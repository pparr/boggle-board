from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

import numpy as np
import string
import boggle as b

# configuration
DEBUG = True

# app instance
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

board = b.Board()

@app.route('/letters', methods=['GET'])
def letters():
    newBoard = board.getRandomBoard()
    newBoard = newBoard.tolist()
    return jsonify(newBoard)


@app.route('/gridsize', methods=['POST'])
def gridsize():
    response = request.get_json(silent=True)
    board.boardSize = int(response['data']['selected'][0])
    return response['data']['selected'][0]
    

@app.route('/solve', methods=['GET'])
def solve():
    adjacencies = board.AdjacencyMatrix()
    solutions = board.solver(adjacencies)
    return jsonify(solutions)
    

if __name__ == '__main__':
    app.run()