#!/usr/bin/env python3
"""
Script: Traitement des Commissions
Fichier: app/scripts/commissions/process_commissions.py

Traite les commissions des techniciens à partir des factures et des missions associées.
Valide la cohérence des données et gère les cas particuliers.

Usage:
    python app/scripts/commissions/process_commissions.py \\
        --log "reports/ST-001-process_commissions.log"
"""

import sys
import json
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

# Configuration logging
def setup_logger(log_file: str) -> logging.Logger:
    """Configure et retourne un logger."""
    log_path = Path(log_file).parent
    log_path.mkdir(parents=True, exist_ok=True)
    
    logger = logging.getLogger('process_commissions')
    logger.setLevel(logging.INFO)
    
    # Handler fichier
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    
    # Format
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    return logger


def load_invoices(input_file: str = None) -> List[Dict]:
    """
    Charge les factures depuis un fichier JSON.
    
    Args:
        input_file: Chemin vers le fichier JSON
    
    Returns:
        Liste des factures
    
    Raises:
        FileNotFoundError: Si fichier introuvable
        json.JSONDecodeError: Si format JSON invalide
    """
    if not input_file:
        return []
    
    if not Path(input_file).exists():
        raise FileNotFoundError(f"Fichier non trouvé: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_invoice(invoice: Dict) -> Tuple[bool, str]:
    """
    Valide une facture.
    
    Args:
        invoice: Données de la facture
    
    Returns:
        (is_valid, error_message)
    """
    # Champs obligatoires
    required_fields = ['nfacture', 'montant_ht', 'montant_ttc', 'articles']
    
    for field in required_fields:
        if field not in invoice:
            return False, f"Champ obligatoire manquant: {field}"
    
    # Validation montants
    if invoice['montant_ht'] <= 0 or invoice['montant_ttc'] <= 0:
        return False, "Montants invalides (doit être > 0)"
    
    if invoice['montant_ttc'] < invoice['montant_ht']:
        return False, "Montant TTC inférieur à HT"
    
    # Articles
    if not invoice['articles'] or len(invoice['articles']) == 0:
        return False, "Au moins un article requis"
    
    return True, ""


def process_single_invoice(invoice: Dict, logger: logging.Logger) -> Dict:
    """
    Traite une facture unique.
    
    Args:
        invoice: Données de la facture
        logger: Logger pour tracer l'exécution
    
    Returns:
        Dict avec résultat du traitement
    """
    # Validation
    is_valid, error = validate_invoice(invoice)
    if not is_valid:
        return {
            'status': 'error',
            'nfacture': invoice.get('nfacture', 'UNKNOWN'),
            'error': error
        }
    
    nfacture = invoice['nfacture']
    intervenants = invoice.get('intervenants', [])
    articles = invoice['articles']
    
    # Cas 1: Mono-intervenant
    if len(intervenants) == 1:
        return {
            'status': 'ok',
            'nfacture': nfacture,
            'type': 'mono',
            'intervenant': intervenants[0],
            'montant_ht': invoice['montant_ht'],
            'montant_ttc': invoice['montant_ttc'],
            'articles': articles,
            'date_traitement': datetime.now().isoformat() + 'Z'
        }
    
    # Cas 2: Multi-intervenant - Tentative de mapping
    if len(intervenants) > 1:
        # Essayer de mapper articles aux techniciens
        mapped = attempt_article_mapping(articles, intervenants)
        
        if mapped['success']:
            return {
                'status': 'ok',
                'nfacture': nfacture,
                'type': 'multi',
                'intervenants': mapped['result'],
                'montant_ht': invoice['montant_ht'],
                'montant_ttc': invoice['montant_ttc'],
                'date_traitement': datetime.now().isoformat() + 'Z'
            }
        else:
            # Conflit détecté
            return {
                'status': 'conflict',
                'nfacture': nfacture,
                'type': 'conflit',
                'raison': mapped['error'],
                'articles': articles,
                'intervenants': intervenants,
                'montant_ht': invoice['montant_ht'],
                'montant_ttc': invoice['montant_ttc'],
                'date_detection': datetime.now().isoformat() + 'Z'
            }
    
    return {
        'status': 'error',
        'nfacture': nfacture,
        'error': "Pas d'intervenant sur la facture"
    }


def attempt_article_mapping(articles: List[Dict], intervenants: List[str]) -> Dict:
    """
    Tente de mapper les articles à des techniciens.
    
    Args:
        articles: Liste des articles
        intervenants: Liste des techniciens
    
    Returns:
        {'success': bool, 'result': mapping ou 'error': raison}
    """
    # Logique simplifiée: pour chaque article, assigner au premier intervenant
    # En production, cela serait plus complexe (croiser avec types de missions, etc.)
    
    if not articles:
        return {'success': False, 'error': 'Pas d\'articles'}
    
    if not intervenants:
        return {'success': False, 'error': 'Pas d\'intervenants'}
    
    # Essayer une assignation simple: si un seul article par intervenant possible
    if len(articles) == len(intervenants):
        return {
            'success': True,
            'result': [
                {
                    'intervenant': intervenants[i],
                    'montant': articles[i].get('montant', 0),
                    'designation': articles[i].get('designation', '')
                }
                for i in range(len(intervenants))
            ]
        }
    
    # Sinon, conflit
    return {
        'success': False,
        'error': f"Impossible de mapper {len(articles)} articles à {len(intervenants)} intervenants"
    }


def save_commissions(commissions: List[Dict], db_type: str = 'pickledb'):
    """
    Enregistre les commissions dans la base de données.
    
    Args:
        commissions: Liste des commissions valides
        db_type: Type de base ("pickledb" ou "sql")
    """
    if db_type == 'pickledb':
        try:
            import pickledb
            
            db = pickledb.load('app/data/commissions.db', auto_dump=True)
            
            existing = db.get('commissions') or []
            existing.extend(commissions)
            
            db.set('commissions', existing)
            
        except ImportError:
            raise ImportError("pickledb non installé: pip install pickledb")
    else:
        raise ValueError(f"Type de base non supporté: {db_type}")


def save_conflicts(conflicts: List[Dict], db_type: str = 'pickledb'):
    """
    Enregistre les commissions en conflit dans la base de données.
    
    Args:
        conflicts: Liste des commissions en conflit
        db_type: Type de base ("pickledb" ou "sql")
    """
    if db_type == 'pickledb':
        try:
            import pickledb
            
            db = pickledb.load('app/data/conflicts.db', auto_dump=True)
            
            existing = db.get('conflicts') or []
            existing.extend(conflicts)
            
            db.set('conflicts', existing)
            
        except ImportError:
            raise ImportError("pickledb non installé: pip install pickledb")
    else:
        raise ValueError(f"Type de base non supporté: {db_type}")


def process_commissions(input_file: str = None, log_file: str = 'reports/ST-process_commissions.log', db_type: str = 'pickledb') -> Dict:
    """
    Traite les commissions à partir des factures.
    
    Args:
        input_file: Chemin vers fichier JSON (optionnel)
        log_file: Chemin vers le fichier de log
        db_type: Type de base ("pickledb" ou "sql")
    
    Returns:
        Dict avec résultat: {'total': N, 'valides': N, 'conflits': N, 'montant_total': X}
    
    Raises:
        ValueError: Si données invalides
        IOError: Si fichier introuvable
    """
    logger = setup_logger(log_file)
    logger.info("DÉBUT: Traitement des commissions")
    
    try:
        # Chargement
        invoices = load_invoices(input_file) if input_file else []
        logger.info(f"Factures chargées: {len(invoices)}")
        
        # Traitement
        commissions = []
        conflicts = []
        errors = []
        
        for invoice in invoices:
            result = process_single_invoice(invoice, logger)
            
            if result['status'] == 'ok':
                commissions.append(result)
            elif result['status'] == 'conflict':
                conflicts.append(result)
            else:
                errors.append(result)
                logger.warning(f"Erreur sur {result.get('nfacture')}: {result.get('error')}")
        
        # Enregistrement
        if commissions:
            save_commissions(commissions, db_type)
        if conflicts:
            save_conflicts(conflicts, db_type)
        
        # Résumé
        total_amount = sum(c.get('montant_ttc', 0) for c in commissions)
        
        logger.info(f"Commissions valides: {len(commissions)}")
        logger.info(f"Commissions en conflit: {len(conflicts)}")
        logger.info(f"Erreurs: {len(errors)}")
        logger.info(f"Montant traité: {total_amount:,.2f} €")
        logger.info("FIN: Succès")
        
        return {
            'total': len(invoices),
            'valides': len(commissions),
            'conflits': len(conflicts),
            'erreurs': len(errors),
            'montant_total': total_amount
        }
    
    except Exception as e:
        logger.error(f"ERREUR: {str(e)}")
        raise


def main():
    """Point d'entrée du script."""
    parser = argparse.ArgumentParser(
        description='Traite les commissions à partir des factures'
    )
    
    parser.add_argument(
        '--input',
        help='Chemin vers le fichier JSON de factures',
        default=None
    )
    
    parser.add_argument(
        '--log',
        help='Chemin vers le fichier de log',
        default='reports/ST-process_commissions.log'
    )
    
    parser.add_argument(
        '--db-type',
        help='Type de base de données',
        choices=['pickledb', 'sql'],
        default='pickledb'
    )
    
    args = parser.parse_args()
    
    result = process_commissions(
        input_file=args.input,
        log_file=args.log,
        db_type=args.db_type
    )
    
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
