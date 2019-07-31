import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/E893BE40-0CD5-E711-800C-0025905A609E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/4A01D8C1-1FD5-E711-8586-0025905A6076.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/902037F0-31D5-E711-AC79-0CC47A7C35A4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/388716A6-2ED5-E711-A7FC-0025905A48BC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/B6D23AED-2BD5-E711-B668-0CC47A4C8E46.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/0E5B1613-4FD5-E711-99CE-0CC47A7C34E6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/9806280C-23D5-E711-B0BF-0025905B85D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/26AF103E-27D5-E711-B26A-0025905A60DA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/FE96FA4F-25D5-E711-A513-0025905A60B0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/2CF958FA-31D5-E711-BDA0-0CC47A4C8EB0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/223AE08D-44D5-E711-9F62-0CC47A4C8ECA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/94C9644D-40D5-E711-BA0D-0CC47A7C3430.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/C82AF0F0-2BD5-E711-B337-0CC47A7C354C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/02B079F3-0DD5-E711-9401-0025905A48D0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/18B11EB2-29D5-E711-BF43-0CC47A4D7640.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/5C89B149-38D5-E711-ADF3-0025905A60F2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/4A99946B-49D5-E711-96DE-0CC47A4D7664.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/4EA8B212-2BD5-E711-B42B-0CC47A78A4BA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/92F35233-3FD5-E711-A99A-0CC47A7C3458.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/A6ADF9CD-39D5-E711-9BDB-0CC47A4C8E7E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/0C660A45-2AD5-E711-918A-0CC47A7C34A6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/CE3E100B-96D5-E711-8E30-0CC47A4D7606.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/BE0E05A6-50D5-E711-BFC3-0CC47A4C8F18.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/0C4BF772-48D5-E711-A4A4-003048FFD71C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/247C7303-2AD5-E711-A575-0025905B8562.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/04D50A7A-38D5-E711-A8F5-0025905A48FC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/DABE34D5-48D5-E711-BFC0-0CC47A4D76C0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/125F4F00-49D5-E711-B704-0CC47A78A30E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/DC4A8F58-4BD5-E711-B500-0CC47A7C357A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/C0B7D519-4DD5-E711-9CA6-0CC47A4D764A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/E6DD56CE-4DD5-E711-8EC6-0CC47A4C8E70.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/9EF4A817-4DD5-E711-8854-0CC47A4C8E20.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/109DE0A9-4AD5-E711-9761-0CC47A4C8F12.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/0EA30C77-4DD5-E711-993C-0CC47A4D76CC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/301E11CB-4DD5-E711-924A-0CC47A4D7662.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/1038C8AE-4AD5-E711-AD05-0CC47A7C3604.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/8E2536CF-32D5-E711-8137-0025905A608A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/EA7B9996-50D5-E711-A9D2-0CC47A4C8F30.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/985DEDA0-4ED5-E711-91BA-0CC47A78A42C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/CAC71384-62D5-E711-8BCF-0CC47A4D76AC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/2C359EC0-5DD5-E711-98E6-0025905B85FC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/78E0DF28-62D5-E711-8D28-0025905A6076.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/BA44CAF6-4ED5-E711-A79F-0025905B85A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/421E1FEE-4BD5-E711-B316-0025905A60D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/50FB62C6-5DD5-E711-8067-0CC47A4D76D6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/607BCE68-4CD5-E711-A343-0025905B857C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/66497796-83D5-E711-9018-0CC47A7C3430.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/AE182EBC-44D5-E711-9286-0025905A610A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/50000/E824D292-83D5-E711-85A0-0025905A60A6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/905BC25C-48D7-E711-9C92-FA163ED60C82.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B08E026B-A6D7-E711-A1DF-5065F3815221.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/EE72C8C7-25D7-E711-A728-0025901FB100.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8C9583AF-DFD7-E711-BD80-003048CB8584.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C8A0CB34-9AD6-E711-BE45-FA163EC0EA10.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/62C52215-81D6-E711-870A-02163E014F80.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DA4FB3B7-96D6-E711-B1D9-FA163E909D3A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7217AC2D-82D6-E711-9F98-FA163EE0F5F8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D47EAA2C-A1D7-E711-9255-FA163ECD0F5A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1C326F5C-48D7-E711-ADA9-FA163E28726B.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BA7982F4-1BD7-E711-8DE7-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1C45A675-1CD7-E711-8C49-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E427B722-4FD7-E711-A158-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6822C5E7-1BD7-E711-9867-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8E36EAE4-E6D7-E711-852E-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/26EC4E78-A6D7-E711-9C58-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F89213F0-D7D7-E711-A34F-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/70D3F453-7AD8-E711-94EC-008CFAE451A4.root',
] )




















