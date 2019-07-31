import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3A4D620E-E033-E811-B7B8-A0369FE2C1E4.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8A882A4C-0834-E811-A575-A0369FE2C082.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C019DE48-CE32-E811-BB2C-002590DE38C8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/EC423CEB-9A33-E811-8BCF-3417EBE7047A.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/BAAB72B3-CA32-E811-B71D-6C3BE5B594A0.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C61B05B8-A233-E811-9DB7-44A842CFD5E5.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/FC2B6E0B-4B33-E811-846A-001CC47D7BE0.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/96A384C2-7934-E811-AD82-FA163EB4130C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3AFDF3F3-8935-E811-B01F-FA163ECA61EF.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C2CB9F05-8A35-E811-9DE1-02163E01A159.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/6ED386A3-D434-E811-8C0A-02163E019FD8.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C2FF7909-8933-E811-A2E1-7845C4FC39C8.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/74A0A4F4-BB33-E811-8291-008CFAFC5984.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/AECE05BB-B833-E811-9313-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/6ED4B563-B833-E811-A14F-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/16569B70-DE32-E811-89CA-0CC47AF9B302.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/0EECAA7D-DE32-E811-BDDE-0025905C5438.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/B8E80D3E-3C33-E811-BBCA-0025905C96EA.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/488B58B2-B333-E811-AE7A-0025905D1D50.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/D2591B17-1034-E811-8762-0025904C4E2A.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/76206A08-B133-E811-B9D7-0025905C3DD6.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/309C4989-BB33-E811-A8EF-0025905C2CBC.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/AE34F6FB-BD32-E811-B4CD-008CFAC94258.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/B63617D1-FE32-E811-AC7E-008CFAC93CE8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/46E85DB3-F332-E811-B107-008CFAC93E4C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/CA853BCD-2533-E811-BF00-008CFAC940CC.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/1A7A6DDA-ED32-E811-94A3-0090FAA58B64.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/520C94FC-0233-E811-B163-0CC47A4DECE2.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/582FDCD1-7236-E811-A1A0-A0369F83639C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/0EAE05BA-7236-E811-A8DD-A0B3CCEBAA8E.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/58EFF5D6-E232-E811-988A-24BE05C6C7E1.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C0CACF2F-D632-E811-AC9C-E0071B7A45D0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/F41BBE6F-7436-E811-9D17-002590E3A0FC.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/EA9AA785-7336-E811-9441-1866DAEB5230.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/D8F5CB9F-2C32-E811-9A8A-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/86FB4B8F-2C32-E811-891E-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/EC35BCA5-E132-E811-A202-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/BE6103C5-E132-E811-AC05-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E675ADB5-2333-E811-B2CF-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A6528250-1233-E811-8A22-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8AA3889C-2133-E811-BE6F-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/286A8585-1333-E811-A5E8-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3CCE4DF3-0335-E811-AE0D-7CD30AD09DE4.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/74A06572-0335-E811-9184-7CD30AD08824.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/5A868A90-7A36-E811-840A-008CFAC93DFC.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/4A215290-7336-E811-88EF-6C3BE5B5F228.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/4EA1A954-7436-E811-BC19-D8D385FF17CA.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/AC3F65DE-F932-E811-A8C7-001E67E6920C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8E50E9DF-EA32-E811-8FC0-001E67E69E05.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/96F55C34-BC32-E811-B1A5-001E67A3FEB1.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/7C26CA08-D232-E811-B3BB-001517FA7A98.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/364BF074-E332-E811-B23F-1866DAEA7E64.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8A96BF69-E432-E811-81D3-1866DAEA7E28.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C255FD1B-C632-E811-A717-1866DAEB5D80.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/9A2D4BB1-1E33-E811-BF2F-90B11C0BCBC1.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8033B5A6-1E33-E811-A1F8-B083FED177B0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C060A474-B733-E811-B6AD-842B2B1811CC.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/EE271EA2-7236-E811-B542-E0071B7A5540.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/6CC41CA2-7236-E811-9F7B-E0071B7A5540.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2A197727-5633-E811-A6BA-44A842B4D8B1.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2E386780-0234-E811-9DC6-44A842B4CC71.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2627CB29-FB32-E811-9EDB-0025905B858E.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/14EF20AA-0F33-E811-9B33-0025905A60B4.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/9C217A1E-FB32-E811-978B-0CC47A7C340E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C4C45FD5-2933-E811-B61A-0CC47A78A33E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/26CBFC07-FC32-E811-9D58-0CC47A4D762E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3C6CF819-2333-E811-9D42-0CC47A7C353E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/DA463B2C-0F33-E811-9A87-0CC47A4D75F8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A82BE317-2D33-E811-A43E-0CC47A7C353E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/26B606B1-1C33-E811-888A-0CC47A7C34A6.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/D6F6C8BB-2233-E811-A32E-0CC47A7C354A.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/54C5FB8E-2533-E811-ACE5-0CC47A4C8EBA.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/64A24665-2633-E811-8D4F-0CC47A78A446.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A2B8F0F7-7133-E811-8963-0025905A60D0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/78CB9FF8-2433-E811-ABAC-0CC47A7C3430.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/FA4F8657-2E33-E811-974C-002618FDA287.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/7472DABC-0F33-E811-AF34-003048FFD7AA.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/0C4FABA9-5533-E811-A788-0CC47A4D762E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/965D04D7-8B33-E811-BC1F-0CC47A4D75F4.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/D4DB2756-5533-E811-BD88-0025905A48D8.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/1420C2D5-8433-E811-AE6E-0CC47A78A414.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A0F1C9A2-8433-E811-985F-0CC47A7C34A6.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C89C8ED2-B233-E811-8187-0CC47A4D762E.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2ECF063B-8A33-E811-812E-0CC47A7C3636.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/1C5667B9-8B33-E811-B2E7-0CC47A7C3434.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8EC59E9F-5033-E811-AA3B-0025905A60F8.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A093176A-7333-E811-9B79-0CC47ABB5178.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2A0C21D1-7333-E811-8F2A-002590E7DEBE.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/FA4134BA-3835-E811-8A86-549F351EDC46.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8A40893A-3935-E811-ADE9-7845C4F92C96.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/AA2A0F8D-C435-E811-A8D8-44A842B4520B.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/50A8414E-C635-E811-AF9A-00266CF83638.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/4A80B9FC-4C34-E811-8750-549F35AD8BFD.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8477A32E-4E36-E811-829D-B496910A9A30.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3CF9AF81-7336-E811-9D25-008CFA1CB8A8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8C89F85A-1533-E811-84DE-FA163E18BECB.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/F2F2DF64-3B33-E811-AC9D-FA163EA81608.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/AAB3EC66-3B33-E811-8755-02163E019EAF.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/52737F3D-B033-E811-9E83-FA163E15FBFA.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/80333C84-EB33-E811-BEC8-FA163EF4C6B1.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/DA2A360A-0134-E811-BFD8-FA163EB539C9.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/88FEEDAA-FE33-E811-A05B-FA163EDFE3C8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3A732BAF-8134-E811-BFAA-FA163E21A18F.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E05381B7-7934-E811-B78B-FA163E76C639.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/941D46CB-2933-E811-83B9-AC1F6B1AF150.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/B0B5056C-2933-E811-92D1-A0369F836364.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/EE253E70-6B33-E811-9B79-44A84225C3D0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/1ED087FB-6B33-E811-AC60-14187763663C.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/1401AFF3-7F33-E811-B3F3-1418776420DF.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A2D790E3-1634-E811-BB6B-B083FED12B5C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/D06CF8A0-5134-E811-91A0-D48564599CAA.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/7EA148E5-1634-E811-8982-B083FECFC6ED.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/222F76F9-A734-E811-BABE-A4BF0112BC9E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/CE349DE4-8835-E811-AAFA-001E67792680.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/B89D5992-9B33-E811-A72D-008CFAF554E4.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/5C7AC314-B133-E811-A0A7-A0369FD20764.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/4CD066EA-C933-E811-8FE0-008CFAF554E4.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/9E97B608-A733-E811-902F-000AE488BB24.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/A899BDD2-C933-E811-B73E-008CFAF55402.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/AE725451-2A34-E811-8055-848F69FD2556.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/129DD15B-3734-E811-8165-A0369FD20D18.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/BC633CE8-F233-E811-8A50-3417EBE51E7D.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2E481745-F633-E811-AE2A-3417EBE52915.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E0CED4F8-3135-E811-8284-0CC47A7C34A6.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E8567ED0-7436-E811-89A3-0025907D2502.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/70C88BF1-A631-E811-B7B6-FA163EBD49DA.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/3868B30B-1632-E811-A895-FA163E98BEC0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/08678948-0732-E811-89F9-FA163E9C2688.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/CE84328E-7032-E811-B0A3-FA163EF16F81.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/84B1C208-C432-E811-BCCA-FA163E81E325.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E239D51B-E032-E811-9992-FA163E8AC021.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E633E565-C432-E811-9276-FA163E2016C6.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2469DCC0-E032-E811-B932-FA163EAE126B.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/7C3D798B-CA32-E811-AEEA-FA163EAB4AB6.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/4E1734E2-7236-E811-9EDE-002590DE6E1E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/6CE32CAF-7236-E811-BD66-0CC47A5FC285.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/CA8AD7E0-7934-E811-A3EA-0CC47A13CDA0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/BEC15B74-FC32-E811-B1ED-001E67792846.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/CE9AE700-5033-E811-BEEA-A4BF011590D8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/9C96EAC2-1F34-E811-B9A3-001E67792872.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/2C0A86AB-1F34-E811-97A6-001E67E6F8AF.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/44FE6702-2134-E811-812C-001E67792800.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/E823253D-8234-E811-A750-A4BF0112E330.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/9E587FE9-5033-E811-87BF-0025901D40B2.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/7C4B5658-2A34-E811-AAEC-0025901D40A6.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/207B62AE-EB32-E811-923C-0025904A91F6.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/ACAFE3EB-CB32-E811-BF51-0CC47A2B04DE.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/44415A2C-D732-E811-886A-0025901D16B0.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/D644B61B-D832-E811-BB2E-002590491B22.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/C20C8A96-E432-E811-BB16-0025904A8EC4.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/06D3D0BB-EA3D-E811-A24F-001E67504255.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4842A930-F63D-E811-8A86-008CFAF293FE.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0EAB77E5-F83D-E811-A919-A0369FD1EF10.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/2241DA9A-183E-E811-A3BB-008CFAF293FE.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/A425D345-183E-E811-AAC4-A0369FC52358.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/38E501A5-183E-E811-84ED-008CFAF293BC.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CA25E865-3E3F-E811-B5D2-3417EBE52855.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/FEA06A2A-F93D-E811-97C6-7CD30ABD295A.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B6E23F08-F23D-E811-AFC3-10983627C3C1.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/142484A5-073E-E811-9FA9-A0369F5BE308.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/78370D36-F93D-E811-8E5D-7CD30ABD278A.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/6A933A85-F23D-E811-9157-44A842B2D63E.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E217E58E-003E-E811-8ABE-008CFAF5592A.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/94A74AD1-F83D-E811-B582-44A842B2D64B.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E8AF5772-203E-E811-BF6D-44A842BFA958.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0EBDA6FB-1C40-E811-B6DF-D4AE5269F919.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AE4C861D-433E-E811-8E50-44A842B2990B.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/726C220C-203E-E811-B72E-A0369F5BE308.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/ECDBCD37-463E-E811-8451-00266CF8594C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/72976BDE-423E-E811-91B8-44A842B420FE.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/ECD0FE04-4E3E-E811-BFE6-3417EBE465DD.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AC765532-463E-E811-9F9B-00A0D1EC7FB8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/98624A1D-433E-E811-8D3C-7845C4FB82F2.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F0021912-403F-E811-9316-0CC47A4D9A26.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/287A9F13-403F-E811-976B-0CC47A4DEF3A.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/20A26BED-D83F-E811-A396-0CC47A78A4B8.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/583208A7-1E40-E811-851D-0025905B85AA.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/FA231D1D-5441-E811-93BB-441EA1733A74.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D4BB7190-EB3D-E811-86AB-FA163EC6DE18.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CAEF2680-EA3D-E811-A4B1-0025904CF710.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/30889233-3F3F-E811-9007-28924A35056E.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/2291D192-413F-E811-97EC-28924A35059A.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/24D194B0-413F-E811-87CC-0026B94DBDBC.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B41CD3A5-333E-E811-85EC-3417EBE2F4B1.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/88400A4F-333E-E811-BCCC-008CFAFBEBF2.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/96F22CB1-423F-E811-804A-7CD30AD09B20.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/5819AC7E-443F-E811-A865-509A4C70A05D.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F6B390AD-EA3D-E811-B080-1CB72C1B649A.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/C499F0A4-443D-E811-9B15-6CC2173D6140.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DEB4EFA2-443D-E811-8DFF-6CC2173C4580.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/5850936E-5C37-E811-BF0D-1866DA87A870.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/C040A4A7-5541-E811-9474-001E67504AA5.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CCF36593-513D-E811-9621-0CC47A4D99F0.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9A6EDA04-AF3D-E811-AF36-0CC47A4D9A3A.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F6116E30-AF3D-E811-8DB5-48FD8EE73AFB.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/287C008D-C43D-E811-9F7E-0CC47A4DEE88.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/7E051E3B-C43D-E811-BCF5-0CC47A4DEE12.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/38836976-C43D-E811-8C85-48FD8EE739D1.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/34E646D5-C43D-E811-87D0-0CC47A4D9A42.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E0C72C04-2C3E-E811-8F03-0CC47A4D9A5E.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/32F15CD1-EA3D-E811-8EA1-1866DAEA7EA8.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B4605EC2-423E-E811-B9AE-44A842CFC9A5.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/1664D680-423E-E811-A671-44A842CFCA27.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/28850B94-EA3D-E811-BC55-002590207C28.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F8FE6D21-CA3D-E811-9DF0-B083FED04276.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/C04C8D45-D53D-E811-A014-44A84225C8DB.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/08050F06-CA3D-E811-A414-141877636851.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/A65BCD1F-D53D-E811-A525-44A84225CDFE.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/446E3FB9-E63D-E811-9C56-141877638819.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DA775FBC-C93D-E811-8B33-002590747D9C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9EEA959B-E63D-E811-9736-00259057490C.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/42D7B68C-203E-E811-B0AF-44A84225C8DB.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/802897F0-1F3E-E811-B226-B083FED04276.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4C0D2BDC-3B3D-E811-A99E-A4BF01013F33.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0E6E4AA9-853E-E811-8F77-A4BF010122D7.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/062C3F05-4D3E-E811-AD38-509A4C72D4C6.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/26256867-4E3E-E811-9166-7CD30AD0A7D4.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9C0A3C9B-1C3F-E811-9387-509A4C7480E6.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/2C678BD1-193E-E811-9322-0025905C54DA.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/BEBAA6AD-323E-E811-B929-0025905C5476.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/3CF32672-193E-E811-8379-0025905C54C4.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DE962FCE-323E-E811-8E2F-0025905C42FE.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D0D444B1-323E-E811-A44D-0025905C5484.root',
'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DAF31CBA-323E-E811-8991-0025905C3DD6.root',
#'/store/mc/RunIIFall17DRPremix/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/40EFB09E-5541-E811-9A36-A0369F83628A.root',
] )




















