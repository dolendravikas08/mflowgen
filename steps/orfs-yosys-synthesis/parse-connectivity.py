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
SYNTH_V = RESULTS_DIR + '/synth_output.v'
SYNTH_SDC = RESULTS_DIR + '/synth_output.sdc'

# prepare next file inputs
if next_step == '4-orfs-openroad-floorplan':
  FLOORPLAN_INPUT_V = RESULTS_DIR + '/floorplan_input.v'
  FLOORPLAN_INPUT_SDC = RESULTS_DIR + '/floorplan_input.sdc'

  shutil.copy(SYNTH_V, FLOORPLAN_INPUT_V)
  print(f"Copied {SYNTH_V} to {FLOORPLAN_INPUT_V}")

  shutil.copy(SYNTH_SDC, FLOORPLAN_INPUT_SDC)
  print(f"Copied {SYNTH_SDC} to {FLOORPLAN_INPUT_SDC}")

