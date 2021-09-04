from .autodh import create_dh_table, DHTable, Joint
import numpy as np


# Python 2/3 compatibility
try:
    input = raw_input
except NameError:
    pass


def get_dh_table(robot, base_link, ee_link, modified_dh, validate):
    chain = robot.GetChain(base_link.GetIndex(), ee_link.GetIndex())
    indices = [j.GetJointIndex() for j in chain if not j.IsStatic()]
    lower, upper = robot.GetDOFLimits(indices)
    dof_values = robot.GetDOFValues(indices)

    # Include zero in joint limits and set joint values to zero
    robot.SetDOFLimits(-np.pi * np.ones(len(indices)), np.pi * np.ones(len(indices)), indices)
    robot.SetDOFValues(np.zeros(len(indices)), indices)

    # Create list of Joints
    joints = []
    for j in chain:
        if j.IsStatic():
            continue
        axis = j.GetAxis()
        anchor = j.GetAnchor()
        joint_type = j.GetType()
        joints.append(Joint(axis, anchor, joint_type))

    # Get base and ee frames
    base_frame = base_link.GetTransform()
    ee_frame = ee_link.GetTransform()

    # Restore joint limits and previous dof values
    robot.SetDOFLimits(lower, upper, indices)
    robot.SetDOFValues(dof_values, indices)

    # Create DH tables
    if not modified_dh:
        dh = create_dh_table(joints, base_frame, ee_frame, DHTable.Convention.Standard)
    else:
        dh = create_dh_table(joints, base_frame, ee_frame, DHTable.Convention.Modified)

    # Test random configuration
    if validate:
        rand_dof_values = np.random.rand(len(joints)) * (upper - lower) + lower
        robot.SetDOFValues(rand_dof_values, indices)
        ee_transform = np.linalg.inv(base_link.GetTransform()).dot(ee_link.GetTransform())

        assert np.allclose(dh.forward(rand_dof_values), ee_transform)

    return dh
