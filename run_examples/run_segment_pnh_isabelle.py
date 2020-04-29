
import os
import os.path as op

import json
import pprint

import nipype.pipeline.engine as pe

from nipype.interfaces.utility import IdentityInterface
import nipype.interfaces.io as nio

###############################################################################
#Running workflow
#==================

from macapype.utils.utils_tests import load_test_data, format_template
from macapype.pipelines.full_pipelines import create_full_segment_pnh_subpipes


from macapype.utils.utils_tests import load_test_data

package_directory = os.path.dirname(os.path.abspath(__file__))
params_file = '{}/../workflows/params_segment_pnh_isabelle.json'.format(package_directory)
params = json.load(open(params_file))

print(params)
pprint.pprint(params)

if "general" in params.keys() and "data_path" in params["general"].keys():
    data_path = params["general"]["data_path"]
else:
    data_path = "/home/INT/meunier.d/ownCloud/Data_tmp/isabelle"
    #data_path = "/hpc/crise/meunier.d/"
    #data_path = "/hpc/neopto/USERS/racicot/data/"


if "general" in params.keys() and "template_name" in params["general"].keys():
    template_name = params["general"]["template_name"]
else:
    template_name = 'NMT_v1.2'

template_dir = load_test_data(template_name)
params_template = format_template(template_dir, template_name)
print (params_template)


#data_path = load_test_data("data_test_macapype", path_to = my_path)

# data file
T1_file = op.join(data_path, "sub-ziggy_T1w.nii")
T2_file = op.join(data_path, "sub-ziggy_T2w.nii")

# running workflow
segment_pnh = create_full_segment_pnh_subpipes(params=params,
                                               params_template=params_template,
                                               name = "segment_pnh_subpipes_ziggy")
segment_pnh.base_dir = data_path

segment_pnh.inputs.inputnode.T1 = T1_file
segment_pnh.inputs.inputnode.T2 = T2_file

segment_pnh.write_graph(graph2use="colored")
#segment_pnh.run()

exit()