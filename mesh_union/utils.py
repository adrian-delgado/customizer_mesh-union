import time
import trimesh
import pymesh
from mesh_union.logger import logger

def dict_to_tuple(_dict):
    return (_dict['x'], _dict['y'], _dict['z'])

def union(meshes):
    start_time = time.time()

    union_mesh = pymesh.CSGTree({
        "union": [{"mesh": trimesh_to_pymesh(mesh)} for mesh in meshes]
    }).mesh

    end_time = time.time()

    total_time = end_time - start_time

    logger.debug("Union of {} files. Time taken: {:6.2f}".format(len(meshes), total_time))

    return pymesh_to_trimesh(union_mesh)

def trimesh_to_pymesh(trimesh_mesh):
    return pymesh.form_mesh(trimesh_mesh.vertices, trimesh_mesh.faces)

def pymesh_to_trimesh(pymesh_mesh):
    return trimesh.Trimesh(
        vertices = pymesh_mesh.vertices,
        faces = pymesh_mesh.faces
    )


def load_mesh(path, file_type = 'stl'):
    return trimesh.load(path, file_type = file_type)

# def save_mesh(file_name, mesh):
#     mesh.export(path.join(OUT_DIR, file_name))