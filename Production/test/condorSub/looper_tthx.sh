#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15v2

#### Spring15 rare backgrounds - tt/H+X
SAMPLES=(
Spring15v2.WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring15v2.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring15v2.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15v2.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15v2.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext1 \
Spring15v2.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext2 \
Spring15v2.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext3 \
Spring15v2.TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15v2.TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8_ext1 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
