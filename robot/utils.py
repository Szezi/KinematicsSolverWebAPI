from robot.robotic_arm import RoboticArm


def calculate_ik(links, x, y, z, alpha):
    Robot_IK = RoboticArm(links)
    Robot_IK.ik_solver(x, y, z, alpha)
    config_1 = Robot_IK.ik_get_config1()
    config_2 = Robot_IK.ik_get_config2()
    return config_1, config_2
