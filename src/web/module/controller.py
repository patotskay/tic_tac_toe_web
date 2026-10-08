from flask import request, jsonify
from web.model.game import GameWeb
from web.model.field import FieldWeb
from web.mapper.game_mapper import GameWebMapper

def post_game(uuid, service):
    try:
        
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Пустой запрос'}), 400

        field_web = FieldWeb(data['field'])
        game_web = GameWeb(uuid, field_web)

        mapper = GameWebMapper()
        game_domain = mapper.to_domain(game_web)

        updated_game = service.make_move(uuid, game_domain.field.field)

        updated_web = mapper.to_web(updated_game)
        return jsonify({
            'uuid': updated_web.uuid,
            'field': updated_web.field.field
        }), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_game(service):
    game = service.create_game()
    mapper = GameWebMapper()
    game_web = mapper.to_web(game)
    return jsonify({
        'uuid': game_web.uuid,
        'field': game_web.field.field
    }), 201