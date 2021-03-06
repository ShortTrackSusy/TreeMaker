import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/046B87CA-2DEA-E811-B274-001E67E69E32.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/066A1537-28EA-E811-BB58-001E67DDC2CC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/06EBA189-22EA-E811-B562-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0A6755FE-38EA-E811-8311-001E67DFFF5F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0C483EA7-23EA-E811-9368-001E67A3AEB8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0E57D8A7-27EA-E811-84D0-001E67D195F0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/12DCA10C-39EA-E811-95F4-001E675A67BB.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/1A1AEEA4-27EA-E811-B31B-001E67DFFB31.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/1ADCD1BC-28EA-E811-8C1D-485B3919F0B9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3CF79FFB-38EA-E811-80A4-001E67E68BBD.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/42963FAE-23EA-E811-8BF1-001E67A4055F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/466EDBEE-2EEA-E811-BD3C-001E67E0061C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4AC47A74-28EA-E811-9751-001517FB20EC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4C8948A8-23EA-E811-BD7F-001E6758651B.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4EB4E4A3-22EA-E811-AB57-001E67A40442.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/52CF8EB2-27EA-E811-A459-001E675A5262.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/52F86FC1-27EA-E811-888A-A4BF010114DB.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/5CF605C9-27EA-E811-8CA1-A4BF01025568.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/70B302E5-2EEA-E811-82ED-001E67DFFF5F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/72DC7BB5-28EA-E811-B9E2-0026182FD7A3.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/7677A63B-2EEA-E811-8B25-A4BF0102572F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/7837E7BB-23EA-E811-8C0C-A4BF01013F29.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9AFD7D7A-31EA-E811-8E7E-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A2BBCCB0-31EA-E811-B7DF-001E67A3EBD8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/AA5139A1-31EA-E811-A9C8-001E67DFF67C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B890413C-28EA-E811-872F-001E67DDD22B.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/BC8AEAA3-3CEA-E811-9A72-90B11C043098.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/C4236240-28EA-E811-8038-001E675A6928.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CE64C79A-22EA-E811-930F-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D8827805-2FEA-E811-B7F9-A4BF01014073.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DC274E56-28EA-E811-9AA9-A4BF01025FF9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E2C7A1A3-31EA-E811-B248-001E67A40442.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E8414EA9-22EA-E811-9E3D-001E67A4055F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/EC5D4A19-32EA-E811-854C-0026182FD77F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/EC8E7C38-32EA-E811-B139-0026181D2917.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F2F1974A-28EA-E811-BCD6-001E675A659A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/FA5E108F-28EA-E811-A79B-EC0D9A04AE30.root',
] )
