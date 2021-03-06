import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DEA0CCAD-D997-E811-BE1C-FA163ED8122F.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C4853114-6B98-E811-8257-FA163E0D6C88.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CC6313EE-7497-E811-8250-008CFA197A80.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/08818DDE-3897-E811-A81F-003048FFD772.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1ADD545D-3898-E811-9364-0CC47A7C351E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8C366B12-089B-E811-A7B8-B8CA3A70A410.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F24C09A1-5B99-E811-ACA8-0025905A60D2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/101E0CC1-CB99-E811-BDE0-0025905B8594.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/68AC037A-A899-E811-9645-0CC47A4C8F30.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/74E28613-6399-E811-AE0E-0CC47A7C3628.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3ABE6893-6499-E811-8944-0CC47A4C8E20.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DC18E993-6499-E811-A8C1-002618FDA207.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8EE86A42-F899-E811-B7DE-0CC47A4D75F6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AAA61607-6399-E811-8001-0CC47A7C3412.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/486AB706-6199-E811-8C7B-0CC47A4D7664.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/34F89A10-A499-E811-8258-0CC47A78A30E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8E57E99-D199-E811-8C67-0CC47A78A414.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2402DA97-6199-E811-B9CE-0025905B859A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/ACC1F996-D299-E811-8DE2-0CC47A4C8E3C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/268991CA-6199-E811-B068-0CC47A4D7670.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F83B3FEC-5D99-E811-922D-0025905A4964.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9A8E8BEE-6099-E811-A950-0025905A60DE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E2A66C07-D499-E811-A239-0025905A60B4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F0CF57D4-D099-E811-B77D-0025905A609A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BA3A1A71-FB99-E811-9A79-0025905A607E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/42A5EE4E-D499-E811-ADC7-0025905A605E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D22CD5F9-6299-E811-BE1D-0CC47A78A4A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0AFEC2F7-999A-E811-8E19-02163E019EE0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0C3B119D-2A9B-E811-B73F-FA163EDF0BCA.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/248B801A-129B-E811-BAA4-02163E01492B.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/50864453-119B-E811-9EC1-FA163EB308B9.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4658DEC6-459B-E811-A175-0025905C3D96.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/82CDE844-619B-E811-9025-0CC47A4D76AC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F02B6668-8F9B-E811-A74E-0CC47A4C8E56.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8E663FC-8B9B-E811-A2B9-0CC47A4D7638.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/30F80928-9D9B-E811-9D9B-0CC47A4C8E96.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8C607154-909B-E811-8783-0025905A60F4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7AC4165D-909B-E811-86B9-0025905B85D0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/02E1BFDC-9F9B-E811-8061-0CC47A4D7616.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/22C462B8-A09B-E811-BA41-0025905A609A.root',
] )




































