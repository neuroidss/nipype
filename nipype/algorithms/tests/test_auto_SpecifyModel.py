# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.algorithms.modelgen import SpecifyModel
def test_SpecifyModel_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    functional_runs=dict(copyfile=False,
    mandatory=True,
    ),
    high_pass_filter_cutoff=dict(mandatory=True,
    ),
    outlier_files=dict(copyfile=False,
    ),
    subject_info=dict(mandatory=True,
    xor=['event_files'],
    ),
    time_repetition=dict(mandatory=True,
    ),
    realignment_parameters=dict(copyfile=False,
    ),
    event_files=dict(mandatory=True,
    xor=['subject_info'],
    ),
    input_units=dict(mandatory=True,
    ),
    )
    inputs = SpecifyModel.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_SpecifyModel_outputs():
    output_map = dict(session_info=dict(),
    )
    outputs = SpecifyModel.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value