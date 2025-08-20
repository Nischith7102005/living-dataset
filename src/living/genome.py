from dataclasses import dataclass
import numpy as np
@dataclass
class Genome:
    latent: np.ndarray
    fitness: float=0.0
    