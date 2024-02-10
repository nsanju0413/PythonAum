import face_vector

def face_vector(input_image):
    faces = face_vector.detector(input_image, 1)
    if not faces:
        return None
    f = faces[0]
    shape = face_vector.predictor(input_image, f)
    face_descriptor = face_vector.face_model.compute_face_descriptor(input_image, shape)
    return face_descriptor
