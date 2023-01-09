# -*- coding: utf-8 -*-

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister
from typing import List, Optional

from .gate import Gate, ROT_DEG, GATES


class Lapin(Gate):

    GATES = GATES

    NUM_QUBIT = 3

    def __init__(
            self,
            name: Optional[str] = "Lapin",
            genome: Optional[List[str]] = None,
            size: Optional[int] = 5
    ):
        super()
        self.name = name
        self.label = name
        self.genome = self._decode(name, genome, size)
        self.gate = lambda qc, qr: [g(qc, qr) for g in self.genome]

    @staticmethod
    def fetch_gate(_):
        pass

    def _decode(
            self,
            name: Optional[str] = "Lapin",
            genome: Optional[List[str]] = None,
            size: Optional[int] = 5
    ):
        # decode from genome
        if genome is not None:
            genome = [Gate(gene) for gene in genome]
            return genome

        # generate at random
        genome_init = sum([
            [
                f"rx{i+1}"
                for _ in range(np.random.randint(0, 180 // ROT_DEG, dtype=int))
            ] for i in range(self.NUM_QUBIT)
        ], [])
        genome_body = np.random.choice(list(self.GATES.keys()), size, replace=True).tolist()
        genome = [Gate(g) for g in sum([genome_init, genome_body], [])]
        return genome