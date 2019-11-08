import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CC3323B6-B5AB-E611-91A9-0025905A60CE.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/32E58B92-C7AB-E611-9257-0CC47A7C35A8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D2203FA5-99AB-E611-86B2-6C3BE5B5E4C0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2802B3E7-9CAB-E611-BEB3-44A842CF061A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AA5C6A37-A0AB-E611-900A-6C3BE5B59150.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/663AE196-A3AB-E611-8DE4-484D7E8DF06B.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/90EAFEA8-A3AB-E611-B2DD-44A842CFC998.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/08003738-A4AB-E611-B5DF-44A842CFCA0D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F0FFDF5B-A4AB-E611-A64A-44A842CFD65A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FAC6C29F-A2AB-E611-ABE7-44A842CFD674.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B09C3FA6-A2AB-E611-A32B-6C3BE5B5C460.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C64B0B2B-A6AB-E611-8149-44A842CFD674.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F2E03A4D-A7AB-E611-88D1-484D7E8DF06B.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5CEF2331-A8AB-E611-AD65-44A842CFC998.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E679BACC-A7AB-E611-AF8E-B499BAAB50A0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7E82E833-A4AB-E611-8379-B499BAAB50A0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/52557DDF-A8AB-E611-92CF-44A842CFCA0D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/16F49B39-A5AB-E611-B276-6C3BE5B5F210.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/502B91BB-ADAB-E611-AA3D-44A842CF0634.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/98F859FD-ABAB-E611-8D11-44A842CFC998.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/48BFE0D4-AEAB-E611-AE59-6C3BE5B56490.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/089D5237-ABAB-E611-9BC2-B499BAABF064.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2648D284-B0AB-E611-A046-44A842CFC998.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9E753563-B0AB-E611-AF41-484D7E8DF06B.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/80BEFD83-B0AB-E611-ADF8-484D7E8DF09F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/446C9FA0-B2AB-E611-A623-001F29081EDC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/74EFBA5D-B3AB-E611-8691-44A842CFD5D8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A44803CD-B3AB-E611-AFE9-B499BAABF064.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/90799DC9-B4AB-E611-A79F-44A842CF060D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FA5AFD2B-B6AB-E611-9D68-484D7E8DF114.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4897CFCB-B4AB-E611-AA8D-44A842CFD5B1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9E017A2D-B6AB-E611-B064-44A842CF0571.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/587C442E-B6AB-E611-A1F5-484D7E8DF0E0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FCE431DA-B5AB-E611-8AA9-001CC4A63C2A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/82B2C7CE-B4AB-E611-9371-001CC47D420E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C89C89CC-BAAB-E611-B014-484D7E8DF0E0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4E0D2014-B4AB-E611-99B1-001CC4A63C5E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2016C45E-B8AB-E611-86F1-B499BAAC3786.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/586B7981-B7AB-E611-A67C-44A842CFD5CB.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A8C9022D-B6AB-E611-AD5A-44A842CFC9F3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7A5D1CAA-B9AB-E611-8418-44A842CFD5BE.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C8C3CCFE-B9AB-E611-B2D9-44A842CF060D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8CEEFEC9-B4AB-E611-A048-44A842CFD5D8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/16915A0F-BAAB-E611-BC65-484D7E8DF114.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/509B6BA3-B7AB-E611-A852-B499BAAC02CA.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/262C13D2-BBAB-E611-8EF3-001CC4A63C2A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/92947E7B-BEAB-E611-B86F-44A842CFD5D8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/54846FAF-BFAB-E611-9D87-44A842CFD5B1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE00D057-C4AB-E611-A156-B499BAAC068A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1E5E19D8-C6AB-E611-8B9F-B499BAAC054A.root',
] )































