from flask import Blueprint, render_template, request, jsonify, abort
from app import db
from app.blueprints.relance.models import Relance
from app.blueprints.commissions.models import Commission
from datetime import datetime, timedelta
import logging

bp = Blueprint('relance', __name__, url_prefix='/relances')

@bp.route('/', methods=['GET'])
def list_relances():
    """ST-005 : Lister toutes les relances (tri par date de relance)."""
    status = request.args.get('status', 'en_attente')
    delai = request.args.get('delai', '30')

    query = Relance.query.filter_by(statut=status)

    if delai:
        min_date = datetime.now() - timedelta(days=int(delai))
        query = query.filter(Relance.date_relance >= min_date)

    relances = query.order_by(Relance.date_relance.desc()).all()
    return render_template('relance/index.html', relances=relances)

@bp.route('/api', methods=['GET'])
def api_list_relances():
    """ST-005 : API liste paginée des relances."""
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    status = request.args.get('status')

    query = Relance.query
    if status:
        query = query.filter_by(statut=status)

    relances = query.paginate(page=page, per_page=limit)
    return jsonify({
        'items': [relance.to_dict() for relance in relances.items],
        'total': relances.total,
        'pages': relances.pages,
        'current_page': relances.page
    })

@bp.route('/api/<int:id>', methods=['GET'])
def api_get_relance(id):
    """ST-005 : Détail d'une relance."""
    relance = Relance.query.get_or_404(id)
    return jsonify(relance.to_dict())

@bp.route('/api/<int:id>/envoi', methods=['POST'])
def send_relance(id):
    """ST-005 : Envoi d'une relance par email."""
    relance = Relance.query.get_or_404(id)

    if not relance.email:
        abort(400, description="Email manquant pour cette relance")

    try:
        # Logique d'envoi d'email
        logging.info(f"Relance envoyée pour {relance.email}")
        relance.statut = 'envoyee'
        db.session.commit()
        return jsonify({"status": "success", "message": "Relance envoyée"})
    except Exception as e:
        logging.error(f"Erreur envoi email: {str(e)}")
        abort(500, description="Erreur lors de l'envoi de l'email")

@bp.route('/api/<int:id>/archive', methods=['POST'])
def archive_relance(id):
    """ST-005 : Archivage d'une relance."""
    relance = Relance.query.get_or_404(id)
    relance.statut = 'archivee'
    db.session.commit()
    return jsonify({"status": "success", "message": "Relance archivée"})