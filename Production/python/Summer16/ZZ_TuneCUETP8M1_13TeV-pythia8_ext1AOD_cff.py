import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8AFEC8EB-18DA-E611-B4C5-0025905C42F2.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D0883FF0-18DA-E611-BD08-0025905C3D3E.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/54A1A495-2BDA-E611-BC56-0025904CDDF8.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CAC5503A-31DA-E611-A175-0025905C53B0.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B8D833E7-3BDA-E611-B47F-0025905C42A4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FCE31F75-3BDA-E611-B622-0025905C3E68.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B2D3D8E8-3BDA-E611-8CEE-0025905C9726.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/00EE2296-40DA-E611-AF33-0025905C94D2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5C270661-1ADB-E611-8FD0-0025905C2D9A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/747A7108-C2D8-E611-8DFB-0CC47AD98B94.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2C6E053F-E2D8-E611-A539-0CC47A13D416.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CEC774C3-15D9-E611-A90B-90B11C26815F.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/DCA07304-26D9-E611-97DE-002590488694.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CE6141AA-17DA-E611-A411-0025901D08E4.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EC6E8740-41DB-E611-A3A0-0CC47A6C0758.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1A1A0436-4FDC-E611-A5DE-0CC47A13CCFC.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/BE93C478-F4D9-E611-B267-001E67E6F9BD.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4223EB75-F4D9-E611-AC0D-001E67792736.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/42A91F9C-F5D9-E611-BDB1-001E67E7188A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4E09A767-F5D9-E611-9A59-002590A371AA.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9C613144-01DA-E611-97E9-002590A3716C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C4B71A64-29DA-E611-B014-001E67E6F404.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A0658712-F2DA-E611-993A-001E677927CE.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/52AA4CAF-CFDB-E611-8D14-001E67398142.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/36464E1B-71D9-E611-846E-0090FAA57E54.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CAFCF46E-08DA-E611-9E33-002590747E14.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2CB7F954-1ADA-E611-BFB5-0090FAA57AF0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3E385A26-3CDA-E611-B8FE-0090FAA576A0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/707CE907-05DA-E611-A014-A0369FC5B84C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/707CF79B-17DA-E611-B96B-008CFA197B44.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F4E615EB-77DC-E611-9E9D-A0369FC5B438.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/307810BC-97D8-E611-9BE1-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A8739A98-A4D8-E611-BBD6-5065F37D9171.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7EEF0D32-DCD8-E611-A40A-24BE05C4D8C1.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7294905A-FCD8-E611-903B-24BE05C4D8C1.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8C4C0C5B-12D9-E611-ACB6-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/10557F5F-17DA-E611-9C2A-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/DC279682-37DC-E611-A2A1-5065F381E151.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9CF40F2E-3CDA-E611-BAC6-001E675813C4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/242281CC-15DC-E611-98A1-001E67504FFD.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7C69D2FC-A1D9-E611-A365-6CC2173BBF40.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/16EE0657-B3D9-E611-96F4-008CFA051EC0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7EF4775B-10DA-E611-BCC6-C4346BC85718.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/945CD3A1-40DA-E611-96AC-001E67F337BC.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C2FE3BA4-0DDC-E611-9BF8-6CC2173BBD70.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1202B0DE-B2DA-E611-877C-002590E7E004.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1A214EF7-07DA-E611-A71F-0026B94DBDAF.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5C8364FB-F2DA-E611-8B49-0023AEEEB703.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A633AD0F-FADB-E611-AC72-0026B94DBE24.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/48111807-A6DA-E611-B1D5-68B59972C052.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EAC6912E-07DB-E611-960F-C81F66C0F057.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A8830BDC-77DC-E611-B709-008CFAF5592A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/50D42774-B5D8-E611-8E9B-0CC47A7C354C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0827677F-B5D8-E611-BD4D-0CC47A78A4B8.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/DEE31BBE-B6D8-E611-B0B2-0025905A48E4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/06ABF73C-C2D8-E611-B536-0CC47A4C8E96.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/32B45A8F-C3D8-E611-9251-0025905B859A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C05967C0-B6D8-E611-8E9C-0025905A612A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/76A19141-B8D8-E611-BF07-0CC47A7C3424.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E4A0A881-B7D8-E611-A9D0-0025905A60A6.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/50A665BD-B6D8-E611-AE76-0025905A609A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4854E2C9-B9D8-E611-A599-0025905A48F0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5E879BCC-B9D8-E611-B1B0-0CC47A4D767E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E890975D-C1D8-E611-B365-0025905B855C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/30EF865D-D6D8-E611-B703-0CC47A4D7670.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B0A0906D-DBD8-E611-B60D-002618FDA21D.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8C2E89C9-E0D8-E611-BCEE-0025905B85CA.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/6C8B208B-E1D8-E611-90CE-0CC47A4C8EE2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/448ABF8D-E1D8-E611-BFF0-0CC47A78A3E8.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/BAC8ACA8-E8D8-E611-A07B-0CC47A7C354C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/DCDE4EDD-E8D8-E611-A2FA-0CC47A4C8E1C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3CE51BCB-EAD8-E611-ADD0-0CC47A4C8E2E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4C5C0E88-EBD8-E611-A0A1-003048FFCBB8.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/DE8498F0-1AD9-E611-82DB-0CC47A7452D0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5C3DC6AF-1AD9-E611-BF88-0025905A60E0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/52DDE92A-12DA-E611-8C89-0CC47A78A340.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/BE7CA022-12DA-E611-A03B-0CC47A4D762E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3600ACAF-EBDA-E611-99BE-0025905A60B6.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7654153C-EEDA-E611-A77D-0CC47A7C34A0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C80F7BA0-B9D8-E611-9C24-001E67E95B98.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5AC2EE46-C4D8-E611-A709-02163E00E5E2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8802D918-85D9-E611-9519-02163E0176C6.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D85F22A8-9AD9-E611-AEE1-FA163EADF985.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8461B03C-65DA-E611-B962-FA163E272887.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C8CB6411-BFDA-E611-8E70-FA163E511E73.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/AA7D9A11-15D9-E611-ADBD-848F69FD3E2A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/32D52C07-17D9-E611-80B1-00266CF9C22C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9CD3259D-1AD9-E611-8F05-848F69FD29E2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/864D93F2-ACD9-E611-A228-7845C4FC3647.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/36C26079-79DA-E611-8E92-001D09FDD6AB.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F2D6FD76-D5DB-E611-BBCF-008CFAF0842A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E2B361AB-74DC-E611-985E-848F69FD4E8C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4CAE228A-B4D9-E611-9BA1-008CFA165F5C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E2DB112E-80DA-E611-BE2A-008CFA1113F4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/069A9DE5-F6D9-E611-87DC-44A842CF0571.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D84932BA-D5D8-E611-9DE0-ECF4BBE16230.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7210E798-EBD8-E611-BABA-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/86CA4684-F5D8-E611-8F4F-ECF4BBE1BE70.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/48EF9A0E-30D9-E611-BA94-0242AC130004.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/540D1A5F-67DA-E611-91E4-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CE7149EB-DFDB-E611-B24F-ECF4BBE16230.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9A21CC28-73DA-E611-81D5-0CC47A5FBDC5.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E476511E-75DC-E611-B152-0025B3268576.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/00105BC9-C2D9-E611-AF65-0019B9CB01A7.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CE524ED1-C5D9-E611-B590-141877410522.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/760A3E3A-C7D9-E611-8F96-14187741278B.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A4AB036D-90DA-E611-8677-782BCB539B52.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D0591ED8-79DC-E611-B5F6-B083FECF837B.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2C876311-8DDA-E611-B019-0CC47AC08B24.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D28D036F-93D9-E611-BC62-D48564594FB4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D8479139-55DC-E611-BA78-20CF3027A5A2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3CFB8A06-A6DA-E611-B0C6-0CC47A7EEDB0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B0695B2D-0CDC-E611-92F6-0CC47A00941C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7A74C509-D6D8-E611-AEE9-0CC47A0AD668.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9E18BCAB-A1D9-E611-AC1A-002590791DA2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EC318F3B-FEDA-E611-A9F0-002590D9D9BC.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8C8B78C2-33DC-E611-A42C-002590D9D84A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F2E97DB6-ABD8-E611-8892-001E67A3FB91.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B63FB1EF-B1D8-E611-8BF3-A4BF01025B0D.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9EA48487-B8D8-E611-8008-90E6BA3BD76E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F8AFAC56-BBD8-E611-895A-001E67E0061C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/88BDA680-BDD8-E611-BC8D-90E6BA3BD76E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/AAF1CD9D-BED8-E611-A051-001517FB1D0C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D289186E-D9D8-E611-8DE1-A4BF01026229.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0EA7E06F-D9D8-E611-B26B-A4BF0102572F.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1894CD6D-D9D8-E611-94CA-001E67DDCC81.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/964BB16D-D9D8-E611-BFC0-001E67DDCC81.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E2682BFC-E4D8-E611-8E55-485B3919F0B5.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/444A97F9-E7D8-E611-B52D-001E67A42A71.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FC639A72-EAD8-E611-AFA1-001E67DFF6E0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/AED94A58-EBD8-E611-8099-001E67E6920C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E2167D11-EED8-E611-95E1-001E67DFF6E0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/16AFAAAF-6ED9-E611-8A74-A4BF01013F33.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A22DC65C-FAD9-E611-BB26-001E67A3FD26.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4EA99F02-F3DA-E611-8C81-A4BF01025C16.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9AD069CD-68DA-E611-A4F4-3417EBE51A24.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0AB54352-A4DC-E611-9913-008CFAF29334.root',
] )




































