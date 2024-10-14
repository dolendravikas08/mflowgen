import yaml
import shutil

with open( './configure.yml' ) as fd:
    try:
      data = yaml.load( fd, Loader=yaml.FullLoader )
    except AttributeError:
      # PyYAML for python2 does not have FullLoader
      data = yaml.load( fd )

next_step = data['edges_o']['flow-checkpoint.tar.gz'][0]['step']
print(f"Neighbouring node: {next_step}")

RESULTS_DIR = './flow/results/nangate45/gcd/base'
# Output files
ROUTE_ODB = RESULTS_DIR + '/route_output.odb'
ROUTE_SDC = RESULTS_DIR + '/route_output.sdc'

# prepare next file inputs
if next_step == '9-orfs-openroad-finish':
  FINISH_INPUT_ODB = RESULTS_DIR + '/finish_input.odb'
  FINISH_INPUT_SDC = RESULTS_DIR + '/finish_input.sdc'

  shutil.copy(ROUTE_ODB, FINISH_INPUT_ODB)
  print(f"Copied {ROUTE_ODB} to {FINISH_INPUT_ODB}")

  shutil.copy(ROUTE_SDC, FINISH_INPUT_SDC)
  print(f"Copied {ROUTE_SDC} to {FINISH_INPUT_SDC}")

