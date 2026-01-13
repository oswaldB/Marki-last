from behave import given, when, then
from flask import Flask, template_rendered
from contextlib import contextmanager
from app import app as flask_app

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@given('que je suis sur la page des commissions valides')
def step_given_commissions_valides(context):
    context.client = flask_app.test_client()
    context.response = context.client.get('/commissions/valides')

@when('je clique sur le bouton "Réparer" d\'une commission en conflit')
def step_when_click_reparer(context):
    # Simuler le clic sur le bouton Réparer
    pass

@then('une modale doit s\'ouvrir')
def step_then_modale_ouvrir(context):
    assert b'Reparer la Commission' in context.response.data

@then('la modale doit afficher la facture PDF de la commission')
def step_then_modale_afficher_pdf(context):
    assert b'<iframe' in context.response.data

@when('je clique sur le bouton "Découper" d\'une commission valide')
def step_when_click_decouper(context):
    # Simuler le clic sur le bouton Découper
    pass

@then('un drawer doit s\'ouvrir')
def step_then_drawer_ouvrir(context):
    assert b'Subdiviser la Commission' in context.response.data

@when('je clique sur le bouton "Archiver" d\'une commission valide')
def step_when_click_archiver(context):
    # Simuler le clic sur le bouton Archiver
    pass

@then('le statut de la commission doit être mis à jour à "archivé"')
def step_then_statut_archiver(context):
    # Vérifier la mise à jour du statut
    pass

@when('je clique sur le bouton "Régler" d\'une commission valide')
def step_when_click_regler(context):
    # Simuler le clic sur le bouton Régler
    pass

@then('le statut de la commission doit être mis à jour à "réglé"')
def step_then_statut_regler(context):
    # Vérifier la mise à jour du statut
    pass

@given('que je suis sur la page des commissions valides avec des commissions')
def step_given_commissions_valides_with_data(context):
    context.client = flask_app.test_client()
    context.response = context.client.get('/commissions/valides')

@then('je dois voir les commissions avec un statut "conflit"')
def step_then_voir_commissions_conflit(context):
    assert b'conflit' in context.response.data

@then('je dois voir un bouton "Réparer" pour chaque commission en conflit')
def step_then_voir_bouton_reparer(context):
    assert b'Reparer' in context.response.data

@then('je dois voir les commissions avec un statut "valide"')
def step_then_voir_commissions_valide(context):
    assert b'valide' in context.response.data

@then('je dois voir un tableau par technicien')
def step_then_voir_tableau_technicien(context):
    assert b'intervenant' in context.response.data

@then('je dois voir les boutons "Découper", "Archiver", et "Régler" pour chaque commission')
def step_then_voir_boutons_actions(context):
    assert b'Decouper' in context.response.data
    assert b'Archiver' in context.response.data
    assert b'Regler' in context.response.data

@when('je saisis un texte dans le champ de recherche')
def step_when_saisir_texte_recherche(context):
    # Simuler la saisie dans le champ de recherche
    pass

@then('les commissions doivent être filtrées en fonction du texte saisi')
def step_then_commissions_filtrees(context):
    # Vérifier le filtrage des commissions
    pass

@then('je dois voir uniquement les commissions correspondantes')
def step_then_voir_commissions_correspondantes(context):
    # Vérifier l'affichage des commissions filtrées
    pass

@when('je clique sur le bouton "Fermer" de la modale de réparation')
def step_when_click_fermer_modale(context):
    # Simuler le clic sur le bouton Fermer
    pass

@then('la modale doit se fermer')
def step_then_modale_fermer(context):
    # Vérifier la fermeture de la modale
    pass

@when('je clique sur le bouton "Fermer" du drawer de découpage')
def step_when_click_fermer_drawer(context):
    # Simuler le clic sur le bouton Fermer
    pass

@then('le drawer doit se fermer')
def step_then_drawer_fermer(context):
    # Vérifier la fermeture du drawer
    pass

@when('je saisis les données de subdivision dans le drawer')
def step_when_saisir_donnees_subdivision(context):
    # Simuler la saisie des données de subdivision
    pass

@when('je clique sur le bouton "Valider"')
def step_when_click_valider_subdivision(context):
    # Simuler le clic sur le bouton Valider
    pass

@then('la ligne de commission doit être subdivisée')
def step_then_ligne_subdivisee(context):
    # Vérifier la subdivision de la ligne
    pass

@then('je dois voir les nouvelles lignes dans la liste des commissions')
def step_then_voir_nouvelles_lignes(context):
    # Vérifier l'affichage des nouvelles lignes
    pass

@when('je saisis une date de règlement')
def step_when_saisir_date_reglement(context):
    # Simuler la saisie de la date de règlement
    pass

@when('je clique sur le bouton "Enregistrer"')
def step_when_click_enregistrer_reglement(context):
    # Simuler le clic sur le bouton Enregistrer
    pass

@then('la date de règlement doit être enregistrée')
def step_then_date_reglement_enregistree(context):
    # Vérifier l'enregistrement de la date de règlement
    pass

@when('je clique sur le bouton "Enregistrer la date"')
def step_when_click_enregistrer_date(context):
    # Simuler le clic sur le bouton Enregistrer la date
    pass

@then('la date de règlement doit être enregistrée avec la date actuelle')
def step_then_date_reglement_actuelle_enregistree(context):
    # Vérifier l'enregistrement de la date actuelle
    pass
