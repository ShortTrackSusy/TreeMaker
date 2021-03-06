import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/925E47EE-74D6-E611-8869-02163E014400.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/388FCFEE-74D6-E611-A9F5-02163E014311.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/76538FEB-74D6-E611-8D04-02163E019CA9.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/5A59DBF1-74D6-E611-9B9C-02163E0135F3.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/E4AFF3F3-74D6-E611-A7A5-02163E0134D2.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/E8DC0DF9-74D6-E611-9260-02163E01351C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/3693B2F0-74D6-E611-BA24-02163E011B39.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/50308FEE-74D6-E611-883E-02163E014445.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/421452EC-74D6-E611-A5D0-02163E012812.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/74C251EE-74D6-E611-A504-02163E019C60.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/A42FE8F1-74D6-E611-86DB-02163E01430A.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/42E4CBED-74D6-E611-A0CF-02163E013504.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/CC6D2CED-74D6-E611-8E1F-02163E019B7F.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/A675D5EE-74D6-E611-B63F-02163E019E6B.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/E2B852F2-74D6-E611-92E4-02163E0135E8.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/2CD54CFB-74D6-E611-AD9F-02163E0133B1.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/2C2CD7F1-74D6-E611-8176-02163E0138D8.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/BAE5F6EE-74D6-E611-BC8E-02163E019E38.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/F067CEF0-74D6-E611-9204-02163E011C32.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/D0000078-7FD6-E611-BA36-02163E0137DC.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/50A473F5-74D6-E611-91C0-02163E014590.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/DA35BDEF-74D6-E611-A636-02163E019D08.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/6E72A7EE-74D6-E611-94FE-02163E019B3B.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/621228F3-74D6-E611-8670-02163E01370E.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/A6A597ED-74D6-E611-A1F7-02163E019C9C.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/8876EEBE-76D6-E611-B824-02163E0141D4.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/80ACFE5A-93D5-E611-ACC0-02163E019C0A.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/14049E8F-88D5-E611-8613-02163E0144D2.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0A3E235E-8CD5-E611-900F-02163E0144C9.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2694803F-90D5-E611-837F-02163E01422C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0699DB36-90D5-E611-AE84-02163E014106.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E4D79CE4-90D5-E611-9770-02163E01462F.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0AED06E5-90D5-E611-92D6-02163E0145F1.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E21C88E8-90D5-E611-9344-02163E01357C.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0502D6A-92D5-E611-84B8-02163E014445.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DED95F6A-92D5-E611-A88C-02163E013988.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/92E51F72-92D5-E611-B9BF-02163E012260.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E7E6C66-92D5-E611-8DB2-02163E019B89.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5810F463-8BD5-E611-97BE-02163E019B39.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/727CA568-8BD5-E611-B635-02163E019BB9.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/100F478F-88D5-E611-ABF6-02163E019BB0.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC585FAE-89D5-E611-BEC7-02163E0145D2.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5426515D-8CD5-E611-992C-02163E0136FC.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8A3EF080-8AD5-E611-B404-02163E019BEE.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8C95C17B-8DD5-E611-AFBA-02163E011996.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8CA62088-8ED5-E611-AED9-02163E0139C2.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA01B558-8FD5-E611-AE17-02163E01412C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CCF62660-93D5-E611-ADC4-02163E0138D1.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/587CD8EF-90D5-E611-A011-02163E0136D3.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F45138E7-90D5-E611-8FAB-02163E01473D.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/32FDFE76-92D5-E611-96D9-02163E019C01.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/78C7D069-8BD5-E611-909A-02163E019DD1.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8804AAEB-8DD5-E611-A83F-02163E011C7C.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC010654-8FD5-E611-A70F-02163E0134BD.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9A69548A-87D5-E611-B23A-02163E0133E4.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/482C3900-8AD5-E611-8031-02163E01341B.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B26A60F0-8DD5-E611-9D67-02163E014608.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/180BB84A-8FD5-E611-A9B7-02163E019B77.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C0853E74-8AD5-E611-B632-02163E01182A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C889A26C-8BD5-E611-AB30-02163E01270D.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A82B8337-90D5-E611-BF43-02163E0139B4.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2FDA574-8BD5-E611-9DD8-02163E01192C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8C723051-8FD5-E611-990F-02163E0142EE.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6420C884-8ED5-E611-BA05-02163E019D4F.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0ED4BF3-89D5-E611-8B66-02163E014731.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/66D0FE4F-8FD5-E611-9F69-02163E011E30.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3654DB51-8FD5-E611-9BD1-02163E014700.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C63FCD3D-90D5-E611-B1E2-02163E013774.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F24C87E0-90D5-E611-BF15-02163E019BE6.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9E7EC483-87D5-E611-9E01-02163E013925.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9CE1FB67-92D5-E611-ACDD-02163E013490.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C715C35-90D5-E611-BDDF-02163E011A7E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FA4A9C6B-8BD5-E611-B223-02163E019CA5.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/967AE08A-8ED5-E611-99BC-02163E013424.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/964DD3E5-90D5-E611-B288-02163E0138E7.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7481E639-4FD5-E611-A082-02163E01393C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/907E6946-4CD5-E611-9FFF-02163E0119AD.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/482D0185-4BD5-E611-930D-02163E019D5A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/28C2083E-52D5-E611-8B41-02163E019CA1.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96EB5FFD-58D5-E611-B8E6-02163E012694.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BE630033-51D5-E611-9FC6-02163E01356A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F4C92447-4FD5-E611-8D62-02163E019D74.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B6197350-54D5-E611-91A9-02163E01422B.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C8E9A432-4FD5-E611-8B60-02163E019C7E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6CDB6D3B-56D5-E611-AC1C-02163E0139B9.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9CF5CC13-57D5-E611-9ECB-02163E012615.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/72146FA3-53D5-E611-8AA4-02163E019CA3.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E0218B44-52D5-E611-A3E3-02163E014255.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C8C4628F-54D5-E611-9DA2-02163E019E87.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/ECFE9E8B-54D5-E611-AAD3-02163E019C19.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B4EBAB7D-50D5-E611-B5BF-02163E019D8B.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6ADBD1EB-52D5-E611-8EF1-02163E01291D.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/603B169F-55D5-E611-B015-02163E011D82.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/24968841-4FD5-E611-B4CE-02163E011B08.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/66B5A534-51D5-E611-83A0-02163E0119CF.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BE80C29A-55D5-E611-9960-02163E013693.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D4849D3F-52D5-E611-91DE-02163E014360.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/20DC86A7-53D5-E611-AE62-02163E0137EF.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/540A17A1-53D5-E611-80A4-02163E019D76.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5C9CE2EB-52D5-E611-A70A-02163E012512.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3645EE6F-72D5-E611-A6D7-02163E019D04.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/880060E3-52D5-E611-9108-02163E014229.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F67F0144-54D5-E611-A2D8-02163E019E1E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D0F6CCA5-53D5-E611-8DDD-02163E01354D.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2AD829A2-55D5-E611-A7F2-02163E0136BD.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D8D2259E-55D5-E611-BDC6-02163E01442F.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4A69DB90-54D5-E611-A87C-02163E014172.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/222EBBED-52D5-E611-99DB-02163E0144DE.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DC3AB9E2-52D5-E611-8A3D-02163E019BF6.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3063EF2C-51D5-E611-AD02-02163E0143CC.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B4977218-57D5-E611-852F-02163E0136A5.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FE45D39F-53D5-E611-8EFE-02163E019D7C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC45F53B-56D5-E611-B02B-02163E019E2B.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4A65B99C-55D5-E611-BBF3-02163E014786.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-400To600_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C6E138AC-50D5-E611-BAB8-02163E01350A.root',
] )




































