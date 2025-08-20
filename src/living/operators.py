import numpy as np
def add_gaussian_noise(latent: np.ndarray,scale: float=0.05) -> np.ndarray:
    rng=np.random.default_rng()
    noise = rng.normal(loc=0, scale=scale, size=latent.shape)
    return latent + noise