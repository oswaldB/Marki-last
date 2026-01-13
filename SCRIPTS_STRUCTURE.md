# 📁 Structure des Scripts - Récapitulatif

## Hiérarchie Actuelle

```
/home/oswald/Desktop/Marki-last/
├── scripts/                              # Scripts backend organisés par thématique
│   ├── README.md                        # Documentation complète
│   ├── auth/                            # Scripts d'authentification
│   │   └── __init__.py
│   ├── commissions/                     # Scripts de commissions
│   │   ├── __init__.py
│   │   └── process_commissions.py      # ✅ Implémenté
│   ├── relances/                        # Scripts de relances
│   │   ├── __init__.py
│   │   └── fetch_unpaid_invoices.py    # ✅ Implémenté
│   └── fetch_and_import_commissions.py # [LEGACY] À nettoyer
│
├── specs/
│   ├── _app/
│   │   ├── scripts/                     # Spécifications des scripts
│   │   │   ├── commissions/
│   │   │   │   └── process_commissions.spec.md      # ✅ Créée
│   │   │   └── relances/
│   │   │       └── fetch_unpaid_invoices.spec.md    # ✅ Créée
│   │   ├── blueprints/
│   │   ├── templates/
│   │   └── ...
│   ├── specs/
│   │   ├── commissions_specs.md        # ✅ Mis à jour avec bons chemins
│   │   ├── relance_impayees_specs.md
│   │   └── ...
│   └── bdd/
│       ├── auth/
│       ├── commissions/
│       └── relances/
│
└── app/
    ├── data/                           # Fichiers PickleDB
    │   ├── commissions.db
    │   ├── factures_impayees.db
    │   └── conflicts.db
    └── ...

```

## ✅ Étapes Complétées

### 1. **Création de la structure thématique**
   - ✅ Dossier `scripts/auth/`
   - ✅ Dossier `scripts/commissions/`
   - ✅ Dossier `scripts/relances/`

### 2. **Implémentation des scripts**
   - ✅ `scripts/commissions/process_commissions.py` (377 lignes)
   - ✅ `scripts/relances/fetch_unpaid_invoices.py` (362 lignes)

### 3. **Création des spécifications**
   - ✅ `specs/_app/scripts/commissions/process_commissions.spec.md`
   - ✅ `specs/_app/scripts/relances/fetch_unpaid_invoices.spec.md`

### 4. **Mise à jour des références**
   - ✅ `specs/specs/commissions_specs.md` mise à jour avec chemins corrects

### 5. **Documentation**
   - ✅ `scripts/README.md` créé avec guide complet

---

## 📊 Scripts par Catégorie

### **Authentication (auth/)**
*À implémenter*
- [ ] Script de création d'utilisateur initial
- [ ] Script de reset de mot de passe
- [ ] Script de gestion des permissions

### **Commissions (commissions/)**
✅ **process_commissions.py**
- Traite les factures et génère les commissions
- Gère les conflits multi-intervenant
- Stocke dans PickleDB

📌 **Legacy: fetch_and_import_commissions.py**
- Récupère depuis ADN
- À nettoyer/déplacer

### **Relances (relances/)**
✅ **fetch_unpaid_invoices.py**
- Récupère factures impayées depuis ADN
- Enrichit avec données clients
- Stocke dans PickleDB

---

## 🔗 Interconnexions

```
ADN Database
    ↓
[fetch_unpaid_invoices.py] → factures_impayees.db
    ↓
[Web UI: Campaigns] → crée campagnes de relance
    
---

Fichiers JSON/CSV
    ↓
[process_commissions.py] → commissions.db + conflicts.db
    ↓
[Web UI: Commissions] → affichage et résolution de conflits
```

---

## 🚀 Utilisation Actuelle

### Commissions
```bash
cd /home/oswald/Desktop/Marki-last
python scripts/commissions/process_commissions.py \
    --input data/sample.json \
    --log reports/test-commissions.log
```

### Relances
```bash
cd /home/oswald/Desktop/Marki-last
python scripts/relances/fetch_unpaid_invoices.py \
    --log reports/test-relances.log
```

---

## 📝 Fichiers Modifiés dans Cette Session

| Fichier | Action | Details |
|---------|--------|---------|
| `scripts/commissions/process_commissions.py` | ✅ Créé | 377 lignes, validation + traitement |
| `scripts/relances/fetch_unpaid_invoices.py` | ✅ Créé | 362 lignes, PostgreSQL + enrichissement |
| `specs/_app/scripts/commissions/process_commissions.spec.md` | ✅ Créé | Spécification complète |
| `specs/_app/scripts/relances/fetch_unpaid_invoices.spec.md` | ✅ Créé | Spécification complète |
| `specs/specs/commissions_specs.md` | ✅ Mis à jour | Chemins corrigés |
| `scripts/README.md` | ✅ Créé | Documentation |
| `scripts/auth/__init__.py` | ✅ Créé | Placeholder |
| `scripts/commissions/__init__.py` | ✅ Créé | Placeholder |
| `scripts/relances/__init__.py` | ✅ Créé | Placeholder |

---

## 🎯 Prochaines Étapes Recommandées

1. **Nettoyer le legacy**
   - Intégrer/supprimer `fetch_and_import_commissions.py`

2. **Ajouter des tests**
   - `tests/scripts/test_process_commissions.py`
   - `tests/scripts/test_fetch_unpaid_invoices.py`

3. **Implémenter l'orchestration**
   - Scheduler Celery pour l'exécution automatique
   - Dashboard de monitoring

4. **Sécurité**
   - Sécuriser stockage des credentials ADN (.env)
   - Logging des exécutions sensibles
   - Audit trails

5. **Documentation**
   - Comment ajouter un nouveau script
   - Troubleshooting guide

---

## 📞 Support

Consulter les fichiers `.spec.md` pour :
- Format d'entrée/sortie détaillé
- Codes d'erreur possible
- Exemples d'utilisation
- Configuration requise

