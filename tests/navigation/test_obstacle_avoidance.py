import pytest
import numpy as np

# Mock per simulare sensori LiDAR e Camera
class MockLidar:
    def __init__(self, distances):
        self.distances = np.array(distances)

    def detect_obstacle(self, threshold=1.0):
        return min(self.distances) < threshold

class MockCamera:
    def __init__(self, objects):
        self.objects = objects

    def detect_dynamic_objects(self):
        return any(obj.get("dynamic", False) for obj in self.objects)

def fuse_sensors(lidar, camera, threshold=1.0):
    """Fusione LiDAR + Camera per obstacle avoidance"""
    lidar_blocked = lidar.detect_obstacle(threshold)
    camera_dynamic = camera.detect_dynamic_objects()
    return lidar_blocked or camera_dynamic


@pytest.fixture
def lidar_static_obstacle():
    return MockLidar([0.4, 2.1, 1.8])  # Ostacolo statico <1m

@pytest.fixture
def camera_no_threat():
    return MockCamera([])

def test_static_obstacle_lidar_detection(lidar_static_obstacle):
    """Edge case: ostacolo statico rilevato da LiDAR"""
    assert lidar_static_obstacle.detect_obstacle() == True

def test_no_obstacle_fusion(lidar_static_obstacle, camera_no_threat):
    """Edge case: fusione sensori senza minaccia"""
    lidar_safe = MockLidar([2.5, 3.0, 2.8])
    assert not fuse_sensors(lidar_safe, camera_no_threat)

def test_dynamic_obstacle_delta_detection():
    """Edge case: ostacolo dinamico improvviso (delta > 2m/s)"""
    prev = MockLidar([3.0, 3.0, 3.0])
    curr = MockLidar([0.3, 3.0, 0.1])
    delta = min(prev.distances) - min(curr.distances)
    assert delta > 2.0, "Dynamic obstacle not detected by delta"
    camera = MockCamera([{"type": "person", "dynamic": True}])
    assert fuse_sensors(curr, camera) == True