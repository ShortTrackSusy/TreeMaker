import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F8E76494-F2AA-E611-AEF5-0CC47A4D760C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C810C29F-F5AA-E611-8AB8-0CC47A4C8E46.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0A8C7712-FCAA-E611-9857-0CC47A78A4BA.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DAA23DA4-C1AB-E611-AFCD-0CC47A4C8E7E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/04D23748-C5AB-E611-BA70-0CC47A4D761A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/6C758486-E4AA-E611-92C9-549F35AE4FC9.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/867219F5-ECAA-E611-B86B-A0369F7F8E80.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/56DC47C2-EEAA-E611-91A7-549F35AD8BBC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1C12FFAC-F6AA-E611-AE6F-A0369F7F92D4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2866A243-FDAA-E611-9AE5-A0369F7FC0BC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/3C0542DF-04AB-E611-A6A0-A0369F7FC5BC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DC5E9BA1-0DAB-E611-88DB-549F358EB721.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/46F41A80-14AB-E611-8CC6-A0369F7FC070.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DC3E142E-1EAB-E611-A720-549F358EB721.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A2186F06-28AB-E611-B6D8-549F35AE4FA2.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/EC5EA9D3-30AB-E611-829B-008CFA1980B8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/22DAF4B9-39AB-E611-A4FE-549F35AF44D6.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/967D434E-4EAB-E611-ADFC-008CFA0A5808.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/402280E8-27AC-E611-B302-00266CFCC1B4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/EC541B42-3BAC-E611-8AC0-008CFA0A58B4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/5C5B80BF-46AC-E611-B714-549F358EB7BD.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/D493FA58-4BAC-E611-BBA2-549F358EB7E4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1686BAF0-4BAC-E611-8536-549F358EB7BD.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B4ABFEED-4BAC-E611-8195-549F358EB7E4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7402E4A7-4AAC-E611-97B1-008CFA1CB470.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/627377BF-4AAC-E611-8178-008CFA1CB8A8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/FC40315C-4BAC-E611-A9A9-008CFA1CB8A8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9041D440-4DAC-E611-B783-00266CF3DE70.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/62E7ECE4-4FAC-E611-8FD1-549F358EB7E4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DE555461-4FAC-E611-AFCE-008CFA1C64A0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9EC7A45C-4FAC-E611-A4AE-008CFA1CB470.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/982E5B93-51AC-E611-BE01-00266CF3DE70.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2A4C9E12-53AC-E611-AC59-00266CFCC214.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/4AC7D324-52AC-E611-BE7B-549F358EB7E4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A03C70CA-53AC-E611-8D5B-00266CFCC68C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/588DB047-56AC-E611-BB73-549F358EB7E4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F86E5190-54AC-E611-B5FA-00266CFCC1B4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/FA5B1BD4-57AC-E611-9225-008CFA1C64A0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2A73DDC7-55AC-E611-B60E-00266CFCCB44.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1C58E37B-56AC-E611-BF59-00266CF3DF00.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/96A64378-59AC-E611-BC8C-00266CFCCBC8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2CFFFB81-58AC-E611-BCFE-00266CFCC68C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/40AB0C53-5CAC-E611-BD8B-00266CFCC860.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7AEF3632-57AC-E611-B767-00266CFCCD94.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DE9A4B64-5BAC-E611-93CB-008CFA1CB8A8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/260FC5C7-5DAC-E611-92AF-00266CFCCBC8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/4EC79D93-60AC-E611-BF94-008CFA14FA8C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1672086B-51AC-E611-B8CB-008CFA1C64B0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/446764F8-62AC-E611-8DE1-00266CFCC9F8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2C36F2ED-64AC-E611-BDC0-00266CFCCBF0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/FED38AC2-64AC-E611-B573-008CFA14FA8C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1EEC1FF0-64AC-E611-A6D0-00266CFCCDC8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/EE01EDC0-68AC-E611-9D59-A0369F7FC524.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/961D2C6B-66AC-E611-A329-008CFA14FA8C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/061BEFAC-67AC-E611-9045-008CFA14FA8C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/12634152-6CAC-E611-9715-00266CF3DF00.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/386F70EE-6EAC-E611-BF74-00266CFCC68C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/486AC550-75AC-E611-975E-008CFA0F51EC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/80B8FAF7-94AC-E611-8BF7-00266CFBE88C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/72F4B03D-93AC-E611-A718-00266CFCC9F8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/AC899550-95AC-E611-BEF0-0CC47A4D761A.root',
] )











