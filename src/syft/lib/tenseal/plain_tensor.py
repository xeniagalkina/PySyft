# stdlib

# third party
import tenseal as ts

# syft relative
from ...generate_wrapper import GenerateWrapper
from ...proto.lib.tenseal.vector_pb2 import TenSEALVector as TenSEALVector_PB
from ...util import get_fully_qualified_name


def object2proto(obj: object) -> TenSEALVector_PB:
    proto = TenSEALVector_PB()
    # proto.id.CopyFrom(_serialize(obj=self.id))
    proto.obj_type = get_fully_qualified_name(obj=obj)
    proto.vector = obj.serialize()  # type: ignore

    return proto


def proto2object(proto: TenSEALVector_PB) -> ts.PlainTensor:
    # vec_id: UID = validate_type(_deserialize(blob=proto.id), UID)
    vec = ts.plain_tensor_from(proto.vector)
    # vec.id = vec_id

    return vec


GenerateWrapper(
    wrapped_type=ts.PlainTensor,
    import_path="tenseal.PlainTensor",
    protobuf_scheme=TenSEALVector_PB,
    type_object2proto=object2proto,
    type_proto2object=proto2object,
)
