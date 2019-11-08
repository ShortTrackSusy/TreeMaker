import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8085AFBD-FE94-E811-A6BC-002590E39D90.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/ACCD6349-BD95-E811-A0BE-B8CA3A709028.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/80AB2811-649C-E811-9A58-3CFDFE6398E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4A2F2A16-659C-E811-BEE4-3CFDFE63F7E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/36305D9A-439C-E811-9B19-3CFDFE63BDC0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B64405A5-6899-E811-A60D-5065F381F272.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C46CD2D5-6699-E811-822E-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9CE02AED-A599-E811-B3E6-24BE05CE1E31.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/50DF3991-6F9C-E811-BA75-003048CB8584.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1C2DCFCF-689C-E811-A484-008CFAE4534C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4453A62C-6E9C-E811-8478-008CFAC93B84.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2C0C02B7-6E9C-E811-AACE-E0071B7A6850.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/58298D15-6E9C-E811-83D0-1C6A7A26BFE7.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8E82AA38-D09C-E811-BEBC-0CC47AD98D6E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/CCD8B0B2-709C-E811-AAE1-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/E0D3A57C-309B-E811-81E7-24BE05CE1E51.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/08F7170A-DD9E-E811-BB5C-0CC47AD24CF8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D4FC71A6-0F9F-E811-ABA1-3CFDFE63BDE0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0A975C9B-0F9F-E811-BAFD-3CFDFE63C5E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A63AD60B-EB9E-E811-8052-0CC47A78A458.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/E608B017-7E9F-E811-8109-24BE05C626B1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/DE404A99-0F9F-E811-A2BF-EC0D9A8221D6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4A421701-E19E-E811-AC06-EC0D9A8221E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/52E70B1B-0AA1-E811-92C8-44A842CF058B.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/26DBC283-2DA0-E811-A79C-001CC4A63C82.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/52CDCC2D-2EA0-E811-A8A6-44A842CFC9E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0482CEEF-75A1-E811-B318-44A842CFD619.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/BA1CD295-76A1-E811-8FF7-44A842CF058B.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/564104C1-93A2-E811-9F5C-C4346BC70B58.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/600A6C9F-ACA2-E811-8241-C4346BBF3E78.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/ECA9E1A3-1DA5-E811-95C0-B499BAAC055E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/5895B3B3-BDA3-E811-9415-D4AE528E309D.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/662DDA9B-BDA3-E811-9599-3CFDFE639B40.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/68A22A66-2AA5-E811-9E4A-FA163EF034D5.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0A2903B3-18A5-E811-89A2-FA163E1D17CA.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/322E8453-5EA2-E811-8C28-001F2908CE36.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2C1EE039-BDA3-E811-A2D4-001CC4C0B0DC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A6361567-BEA3-E811-ACCF-44A842CFC9B2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0E004ACE-BEA3-E811-9A9E-6C3BE5B59058.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/808AFDF5-BEA3-E811-BC0C-E4115BB4C4BC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/DAA26DBD-BFA3-E811-A13E-6C3BE5B59200.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A64DE884-C0A3-E811-B44B-001F2907EF28.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9C3F168E-41A4-E811-BF62-7CD30AB053DC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D88B02E0-84A4-E811-A04E-24BE05C44BB1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/6857E2FD-16A5-E811-8680-EC0D9A8221EE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B081C9D9-35A6-E811-B34B-24BE05CE3EA1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/72BAA15F-DCA6-E811-A9AC-24BE05C64601.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C4B7A8EE-D8A6-E811-BFDC-7CD30AB053DC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1E79D426-DCA6-E811-A225-008CFAC93CF4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/44210B19-18A6-E811-A8F1-F8C288DA8479.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2E76C2FE-F0AA-E811-B95E-509A4C7489CE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/22A20F07-F4AA-E811-97C0-008CFAFBE8F2.root',
] )































