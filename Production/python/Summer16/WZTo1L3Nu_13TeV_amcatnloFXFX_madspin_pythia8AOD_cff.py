import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/7C26B206-A2C9-E611-B30F-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/34902F15-A4C9-E611-86EA-008CFA1111AC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E2F56548-A4C9-E611-A363-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/1609CD37-A7C9-E611-A30C-008CFA111334.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/963A2E7E-A8C9-E611-923C-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/183C858B-A7C9-E611-A980-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/B065078D-A8C9-E611-91F4-008CFA1111AC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/48CD5AA6-AAC9-E611-9342-008CFA166234.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/A0DFDD5D-ABC9-E611-9C28-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/320D00C6-ACC9-E611-ABB5-008CFA197AC4.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E4A3F208-ACC9-E611-936C-008CFA111334.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/648E915A-B0C9-E611-8AB0-008CFA197AC4.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C82324E6-ACC9-E611-BB13-008CFA111170.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/2C093389-ACC9-E611-B6B2-008CFA1113F8.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/72DE2C5E-AEC9-E611-9E9E-008CFA197448.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/CADD0F87-AFC9-E611-8179-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4485F190-ACC9-E611-BF00-008CFA197D60.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F644378E-ACC9-E611-8510-008CFA19741C.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5021D35F-AEC9-E611-827F-008CFA197B54.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/32AC8E5C-B1C9-E611-A855-008CFA111314.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/9CEAE8BB-B3C9-E611-BB9C-008CFA197448.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/86CF5530-B3C9-E611-ACEB-008CFA111170.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/907FDCBC-B3C9-E611-BEA9-008CFA197A90.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/A61B2B17-B3C9-E611-A1E2-008CFA1113F8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0A503E7D-B5C9-E611-9B58-008CFA111314.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FEFEC2A6-B9C9-E611-B9C6-008CFA197A90.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/B079D45E-B9C9-E611-8E31-008CFA111170.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C6231F02-BBC9-E611-B335-008CFA111314.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4C0DBC74-B9C9-E611-846D-008CFA197448.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/B6CF4752-BAC9-E611-B418-008CFA111270.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0A6D7E52-BAC9-E611-94C1-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F05EA747-BAC9-E611-A9A6-008CFA1113F8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5C154357-BAC9-E611-8D98-008CFA110AEC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/76146B1E-BCC9-E611-B1C6-008CFA197BD4.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/12826491-BEC9-E611-9C74-008CFA111314.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0403040E-C1C9-E611-9830-008CFA1979EC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E80D5DC2-BFC9-E611-B526-008CFA11118C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/B65BB513-BEC9-E611-B06D-008CFA166234.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/16E42A68-C0C9-E611-9DDB-008CFA197448.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/023BFB1A-C3C9-E611-A99A-008CFA110C6C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/64DD7C87-C6C9-E611-8A2B-008CFA197AC4.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5E5DBFA9-C4C9-E611-BC2C-008CFA110B08.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/3092098B-C4C9-E611-94E7-008CFA111314.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/208211C9-C1C9-E611-A84F-008CFA197E8C.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/1A6BC671-C7C9-E611-8D84-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/220F39D7-C5C9-E611-B002-008CFA1979EC.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/8C95A0AB-C6C9-E611-B52E-008CFA111320.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/92F78B3C-C9C9-E611-B22D-008CFA111218.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5E22273C-C9C9-E611-9B17-008CFA111334.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/706E9550-CAC9-E611-BF60-008CFA197AC4.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/647FAF38-C8C9-E611-AEA1-008CFA197488.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5C5219EB-CCC9-E611-BAAB-008CFA110B08.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/306A8A9D-CCC9-E611-A74B-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/CCA6249D-CDC9-E611-A024-008CFA1111EC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/14FCD1E4-CCC9-E611-8BC8-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/342F34A4-CBC9-E611-B8DD-008CFA166234.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/50036EEC-CCC9-E611-AF63-008CFA197CA0.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/6CB07982-D0C9-E611-BCD6-008CFA110B08.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FC94AB96-CFC9-E611-AB81-008CFA111218.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/8C9B0E8D-CBC9-E611-9B64-008CFA197E8C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4863578B-CEC9-E611-B630-008CFA110C78.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F8138E89-CFC9-E611-9F76-008CFA197D88.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/8A27D338-D1C9-E611-BDE6-008CFA110B08.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/04A10B96-CFC9-E611-8273-008CFA197488.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/74920FA2-D1C9-E611-A7F6-008CFA1111EC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/BCB03B29-D1C9-E611-A237-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C6A4F438-D3C9-E611-9FAF-008CFA197CA0.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0211F705-D4C9-E611-8B7B-008CFA110B08.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/DEF953C2-D2C9-E611-AEFB-008CFA197BD4.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/AA840AB8-D4C9-E611-868F-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D2A97D9D-CFC9-E611-8691-008CFA197D74.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/44A7BA6F-D8C9-E611-A124-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/82CF75C7-D2C9-E611-90E4-008CFA11113C.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/54A60530-D7C9-E611-848C-008CFA197488.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C29A52D2-D5C9-E611-8076-008CFA197E8C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0215555E-D3C9-E611-B998-008CFA1112BC.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/9468291B-A2CA-E611-84FF-008CFA197E58.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/A820367D-4FC9-E611-A9F8-008CFA166234.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/8E3FBE72-4FC9-E611-AEE8-008CFA197410.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5A28763B-51C9-E611-A8FD-008CFA197CA0.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/A42493AA-51C9-E611-9646-008CFA1113E8.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/DCDF0AAC-53C9-E611-A9C3-008CFA11136C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/26A8400E-54C9-E611-B25B-008CFA111354.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D0149054-57C9-E611-9A61-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/38E81402-53C9-E611-8084-008CFA197B74.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/1ECA2079-58C9-E611-8C59-008CFA111314.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/16CE4091-5BC9-E611-8FAD-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C089F248-5AC9-E611-A366-008CFA111354.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/AAC7E8CB-5EC9-E611-8297-008CFA1112BC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F0653957-5DC9-E611-8671-008CFA197B74.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/22B5D51D-60C9-E611-AFED-008CFA1113E8.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/96C62E42-62C9-E611-BFE1-008CFA1112BC.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/36F92B64-66C9-E611-BE2A-008CFA1112BC.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/50AA6669-65C9-E611-9F3A-008CFA1111AC.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/52A5431D-64C9-E611-BEC4-008CFA111154.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D60C1F2E-64C9-E611-B123-008CFA197B74.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/82BF0BAB-5FC9-E611-AB46-008CFA111314.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/1CDD5111-6AC9-E611-B618-008CFA1112BC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/18AF5689-6AC9-E611-90B2-008CFA1111AC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/9422E3B8-69C9-E611-B309-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/38F71015-67C9-E611-88F1-008CFA111310.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4A0CBAFC-6DC9-E611-9A59-008CFA197B74.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C453B0E3-6FC9-E611-90F7-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D82ABD3D-73C9-E611-8837-008CFA1979A0.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/EAA1E00C-75C9-E611-8E30-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/7481D5B4-78C9-E611-BA3D-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5C35271A-76C9-E611-9482-008CFA197B74.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/745618B8-7BC9-E611-80F2-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/A8C89194-7FC9-E611-BE09-008CFA197CA0.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E412E6A0-7FC9-E611-8174-008CFA197CD0.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/8EA730A9-7FC9-E611-8C08-008CFA111310.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/32420F3F-81C9-E611-A5A1-008CFA1113E8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/B4A729BC-7FC9-E611-A38C-008CFA1112BC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/7251F5BF-7FC9-E611-A07B-008CFA110DD8.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/88AD2EBA-7FC9-E611-A429-008CFA19741C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/DAABAFA6-85C9-E611-8895-008CFA1979FC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5A346D10-8DC9-E611-A5E5-008CFA111334.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D2AC2CEC-92C9-E611-B204-008CFA111334.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/CA7FFC19-89C9-E611-BFFD-008CFA19741C.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FE9490F9-99C9-E611-B5B1-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/7432ED06-9AC9-E611-A514-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0AA0D951-9BC9-E611-B17B-008CFA197A60.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/6ACB98FD-9FC9-E611-BCD9-008CFA1111AC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FE0595BC-9DC9-E611-ABB5-008CFA111330.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0E2709FB-A0C9-E611-BD38-008CFA111334.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E428E4F7-A0C9-E611-A085-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C6E3B170-BFC7-E611-8770-008CFA1974A0.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/92B5E757-E6C7-E611-AEB7-008CFA111170.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/B6B6D798-EFC7-E611-A96A-008CFA111170.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/AE387522-3FC8-E611-BB77-008CFA110C78.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5CE4A6EC-CAC8-E611-B96C-008CFA111330.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/94581361-3DC9-E611-8EEB-008CFA197E8C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4C4EA3DE-40C9-E611-8673-008CFA197E8C.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D274BF49-44C9-E611-9633-008CFA197CA0.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/CC245D93-49C9-E611-8D0F-008CFA1113F4.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/CA905577-49C9-E611-8A71-008CFA11136C.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/1E696D42-49C9-E611-88AB-008CFA197CA0.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/90EF6E93-49C9-E611-9537-008CFA1111AC.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F67B1519-4EC9-E611-A97A-008CFA197CA0.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D4F2B28F-49C9-E611-830D-008CFA197B74.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E87F1A2D-4EC9-E611-B6A0-008CFA11136C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/489DD86D-4FC9-E611-A9BF-008CFA111354.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/A6D4356C-4FC9-E611-A600-008CFA1113F4.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/94B03778-4FC9-E611-8EAD-008CFA1974D8.root',
#'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/66AA6E29-ACC7-E611-9052-008CFA11118C.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/1E5CE81A-CFCA-E611-8D57-02163E019CD9.root',
'/store/mc/RunIISummer16DR80Premix/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/38DAB3F7-CFCA-E611-9530-02163E019CA0.root',
] )




































