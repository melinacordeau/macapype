:orphan:

.. _api_documentation:

=================
API Documentation
=================

Pipelines
^^^^^^^^^^

----

**Full pipelines** (:py:mod:`macapype.pipelines.full_pipelines`):

.. currentmodule:: macapype.pipelines.full_pipelines

*SPM based*:

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_full_spm_subpipes
    create_full_T1_spm_subpipes

*ANTS based*:

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_full_ants_subpipes
    create_full_T1_ants_subpipes

*ANTS based (intermediate pipelines)

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_brain_extraction_pipe
    create_brain_segment_from_mask_pipe

    create_brain_extraction_T1_pipe
    create_brain_segment_from_mask_T1_pipe

**Data preparation** (:py:mod:`macapype.pipelines.prepare`):

.. currentmodule:: macapype.pipelines.prepare

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_short_preparation_pipe
    create_short_preparation_T1_pipe

    create_long_single_preparation_pipe
    create_long_multi_preparation_pipe

(hidden)

.. autosummary::
   :nosignatures:
   :toctree: generated/

    _create_prep_pipeline
    _create_mapnode_prep_pipeline

----

**Correct bias** (:py:mod:`macapype.pipelines.correct_bias`):

.. currentmodule:: macapype.pipelines.correct_bias

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_correct_bias_pipe
    create_masked_correct_bias_pipe

----

**Register** (:py:mod:`macapype.pipelines.register`):

.. currentmodule:: macapype.pipelines.register

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_register_NMT_pipe

----

**Brain extraction** (:py:mod:`macapype.pipelines.extract_brain`):

.. currentmodule:: macapype.pipelines.extract_brain

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_extract_pipe
    create_extract_T1_pipe


----

**Segment** (:py:mod:`macapype.pipelines.segment`):

.. currentmodule:: macapype.pipelines.segment

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_old_segment_pipe
    create_segment_atropos_pipe

----

**Surface** (:py:mod:`macapype.pipelines.surface`):

.. currentmodule:: macapype.pipelines.surface

.. autosummary::
   :nosignatures:
   :toctree: generated/

    create_nii_to_mesh_pipe
    create_nii_to_mesh_fs_pipe

(hidden)

.. autosummary::
   :nosignatures:
   :toctree: generated/

    _create_split_hemi_pipe

----

Nodes
^^^^^^

**Surface** (:py:mod:`macapype.nodes.surface`):

.. currentmodule:: macapype.nodes.surface

.. autosummary::
   :nosignatures:
   :toctree: generated/

   Meshify

----

**Segment** (:py:mod:`macapype.nodes.segment`):

.. currentmodule:: macapype.nodes.segment

.. autosummary::
   :nosignatures:
   :toctree: generated/

   AtroposN4

----

**Extract brain** (:py:mod:`macapype.nodes.extract_brain`):

.. currentmodule:: macapype.nodes.extract_brain

.. autosummary::
   :nosignatures:
   :toctree: generated/

   T1xT2BET
   AtlasBREX

----

**Correct bias** (:py:mod:`macapype.nodes.correct_bias`):

.. currentmodule:: macapype.nodes.correct_bias

.. autosummary::
   :nosignatures:
   :toctree: generated/

   T1xT2BiasFieldCorrection


----

**Register** (:py:mod:`macapype.nodes.register`):

.. currentmodule:: macapype.nodes.register

.. autosummary::
   :nosignatures:
   :toctree: generated/

   IterREGBET
   NMTSubjectAlign
   NMTSubjectAlign2


----

**Prepare** (:py:mod:`macapype.nodes.prepare`):

.. currentmodule:: macapype.nodes.prepare

.. autosummary::
   :nosignatures:
   :toctree: generated/

   CropVolume

----

Utils
^^^^^^

**Utils tests** (:py:mod:`macapype.utils.utils_tests`):

.. currentmodule:: macapype.utils.utils_tests

.. autosummary::
   :nosignatures:
   :toctree: generated/

   load_test_data

----
