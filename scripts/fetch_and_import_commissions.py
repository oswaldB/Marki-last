#!/usr/bin/env python3
"""
Script to fetch overdue invoices from ADN database and import them into local commissions table.

This script:
1. Connects to the ADN database
2. Executes the SQL query to fetch overdue invoices
3. Connects to the local SQLite database
4. Imports the fetched data into the commissions table

Usage:
    python fetch_and_import_commissions.py
"""

import sqlite3
import psycopg2
from psycopg2 import sql
import os
from datetime import datetime

# Configuration
ADN_DB_CONFIG = {
    'host': 'adn-database-server',
    'database': 'adn_adti',
    'user': 'adn_user',
    'password': 'adn_password',
    'port': 5432
}

LOCAL_DB_PATH = 'app/instance/app.db'

def fetch_overdue_invoices_from_adn():
    """
    Fetch overdue invoices from ADN database.
    Returns a list of dictionaries representing commission records.
    """
    try:
        # Connect to ADN database
        conn = psycopg2.connect(**ADN_DB_CONFIG)
        cursor = conn.cursor()
        
        # SQL query to fetch overdue invoices
        query = """
        SELECT 
            p.nfacture,
            p.idproduitmetier AS ndossier,
            p.refpiece AS reference_piece,
            CASE 
                WHEN p.idcommercial IS NOT NULL THEN 
                    (SELECT prenom || ' ' || nom FROM (ADN_DIAG).Utilisateurs WHERE idUtilisateur = p.idcommercial)
                ELSE
                    (SELECT prenom || ' ' || nom FROM (ADN_DIAG).Utilisateurs WHERE idUtilisateur = p.idusercre)
            END AS intervenant,
            p.totalhtnet AS montant_ht,
            p.totalttcnet AS montant_ttc,
            TO_CHAR(p.datepiece, 'YYYY-MM-DD') AS date_piece,
            '/Reporting/GCO/piece/' || 
            TO_CHAR(p.datepiece, 'YYYY') || '/' || 
            LOWER(TO_CHAR(p.datepiece, 'MM')) || '/' || 
            p.refpiece || '/standard/' || p.refpiece || '.pdf' AS lien_facture,
            'valide' AS statut,
            NULL AS date_reglement,
            NULL AS conflit_detail,
            CASE 
                WHEN EXISTS (
                    SELECT 1 FROM (GCO).GcoPieceVente pv
                    JOIN (GCO).GcoArticle a ON pv.idarticle = a.idarticle
                    WHERE pv.idpiece = p.idpiece
                    AND a.idtypeprestation = 'TECH'
                    GROUP BY pv.idpiece
                    HAVING COUNT(DISTINCT a.idarticle) = 1
                ) THEN TRUE
                ELSE FALSE
            END AS monotech,
            CASE 
                WHEN EXISTS (
                    SELECT 1 FROM (GCO).GcoPieceMetier pm
                    WHERE pm.idpiece = p.idpiece
                    GROUP BY pm.idpiece
                    HAVING COUNT(DISTINCT pm.idmetier) = 1
                ) THEN TRUE
                ELSE FALSE
            END AS mono_dossier
        FROM 
            (GCO).GcoPiece p
        WHERE 
            p.factureavoir = FALSE
            AND p.dateecheance < CURRENT_DATE
            AND (p.facturesoldee = FALSE OR p.facturesoldee IS NULL)
            AND p.valide = TRUE
            AND p.idproduitmetier = 'ADN_DIAG'
            AND EXISTS (
                SELECT 1 FROM (GCO).GcoPieceVente pv
                JOIN (GCO).GcoArticle a ON pv.idarticle = a.idarticle
                WHERE pv.idpiece = p.idpiece
                AND a.commissionne = TRUE
            );
        """
        
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        
        # Convert results to list of dictionaries
        commissions = []
        for row in results:
            commission = dict(zip(columns, row))
            commissions.append(commission)
        
        return commissions
        
    except Exception as e:
        print(f"Error fetching data from ADN database: {e}")
        return []
    finally:
        if 'conn' in locals():
            conn.close()


def import_commissions_to_local_db(commissions):
    """
    Import commission data into local SQLite database.
    """
    try:
        # Ensure the app directory exists
        os.makedirs(os.path.dirname(LOCAL_DB_PATH), exist_ok=True)
        
        # Connect to local database
        conn = sqlite3.connect(LOCAL_DB_PATH)
        cursor = conn.cursor()
        
        # Create commissions table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS commissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nfacture TEXT NOT NULL,
            ndossier TEXT NOT NULL,
            reference_piece TEXT NOT NULL,
            intervenant TEXT NOT NULL,
            montant_ht REAL NOT NULL,
            montant_ttc REAL NOT NULL,
            date_piece TEXT NOT NULL,
            lien_facture TEXT NOT NULL,
            statut TEXT NOT NULL DEFAULT 'valide' CHECK (statut IN ('valide', 'conflit', 'archive')),
            date_reglement TEXT,
            conflit_detail TEXT,
            monotech BOOLEAN DEFAULT FALSE,
            mono_dossier BOOLEAN DEFAULT FALSE
        );
        """
        
        # Insert commissions
        for commission in commissions:
            cursor.execute("""
            INSERT INTO commissions (
                nfacture, ndossier, reference_piece, intervenant, 
                montant_ht, montant_ttc, date_piece, lien_facture, 
                statut, date_reglement, conflit_detail, monotech, mono_dossier
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                commission['nfacture'],
                commission['ndossier'],
                commission['reference_piece'],
                commission['intervenant'],
                float(commission['montant_ht']),
                float(commission['montant_ttc']),
                commission['date_piece'],
                commission['lien_facture'],
                commission['statut'],
                commission['date_reglement'],
                commission['conflit_detail'],
                bool(commission['monotech']),
                bool(commission['mono_dossier'])
            ))
        
        conn.commit()
        print(f"Successfully imported {len(commissions)} commissions.")
        
    except Exception as e:
        print(f"Error importing data to local database: {e}")
        if 'conn' in locals():
            conn.rollback()
    finally:
        if 'conn' in locals():
            conn.close()


def main():
    """
    Main function to fetch and import commissions.
    """
    print("Starting commission import process...")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Step 1: Fetch overdue invoices from ADN
    print("\nFetching overdue invoices from ADN database...")
    commissions = fetch_overdue_invoices_from_adn()
    
    if not commissions:
        print("No overdue invoices found or error occurred.")
        return
    
    print(f"Found {len(commissions)} overdue invoices to import.")
    
    # Step 2: Import to local database
    print("\nImporting commissions to local database...")
    import_commissions_to_local_db(commissions)
    
    print("\nCommission import process completed.")


if __name__ == "__main__":
    main()