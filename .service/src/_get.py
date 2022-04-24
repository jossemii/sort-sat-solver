import numpy
import onnxruntime as rt

import api_pb2
import onnx_pb2
from start import LOGGER
import regresion_pb2


def get_score(model: onnx_pb2.ModelProto, _cnf: dict) -> float:
    session = rt.InferenceSession(
        model.SerializeToString()
    )
    input_name = session.get_inputs()[0].name
    label_name = session.get_outputs()[0].name
    return session.run([label_name], {input_name: [_cnf]})[0][0][0]


def data(cnf: api_pb2.Cnf) -> dict:
    num_literals = 0
    for clause in cnf.clause:
        for literal in clause.literal:
            if abs(literal) > num_literals:
                num_literals = abs(literal)
    return [
        numpy.array((len(cnf.clause))).astype(numpy.int64),
        numpy.array((num_literals)).astype(numpy.int64)
    ]


def cnf(cnf: api_pb2.Cnf, tensors: regresion_pb2.Tensor) -> str:
    LOGGER('GET CNF: selecting a solver ...')
    best_score = None
    for solver_tensor in tensors.non_escalar.non_escalar:
        LOGGER('GET CNF: getting the score for a specific tensor.')
        score = get_score(model = solver_tensor.escalar, _cnf = data(cnf = cnf))
        LOGGER('GET CNF: the score is '+str(score))
        if not best_score or best_score < score:
            LOGGER('     now is the best score.')
            best_score = score
            best_solver_id = solver_tensor.element
    LOGGER('GET CNF finished process.')
    return best_solver_id