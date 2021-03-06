import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/36CCF5AA-13BE-E811-912B-24BE05CE2E81.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/B2D35ED8-62BE-E811-B823-24BE05C6D5A1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/101F6E62-A2BE-E811-944C-E0071B7A8590.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/509B7988-C3BE-E811-B6E3-24BE05C44BC1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/C2122285-E9BE-E811-B5D8-24BE05C6D5A1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/EC993DDE-C3BE-E811-A97E-24BE05BD0F81.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/B4F67484-52BF-E811-8E18-EC0D9A82237E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/1A711761-E9BE-E811-886C-E0071B741D70.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/86352A2E-29BF-E811-BDE0-24BE05BD0F81.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/4E10B5FA-DDBF-E811-895B-14187751C1AB.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/76011300-2FC0-E811-B8BE-90B11C446053.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/92A473D0-86BE-E811-A2F8-A4BF01013F8D.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/344430E8-84BE-E811-BEE9-A4BF010114F4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/1086345B-86BE-E811-9A24-001E67A3FDF8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/8EB61DDC-86BE-E811-B36B-001E675A68BF.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/201D7839-62BF-E811-A053-A4BF0102611B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/A048D36E-62BF-E811-9D8B-A4BF01013F8D.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/281A9B98-81BE-E811-B0CC-06D5D00002CC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/36DB8291-81BE-E811-9EBF-48D539F3863E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/FE9E8F06-92BE-E811-B67A-48FD8EE73A69.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/70A29031-77BF-E811-A005-48FD8EE73A31.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/1A0D25D4-80BF-E811-B7C0-48FD8EE73A59.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/58D22C26-BFBF-E811-8931-AC1F6B0F6758.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/C8BE33EF-E7BF-E811-9E24-C81F66C8BA4C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D4DDCAD2-3AC2-E811-B899-0425C5DE7BEE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/6246A2DF-C0C0-E811-9E3D-0CC47A5FC619.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/8AFF5F7F-00C0-E811-863D-509A4C858ADC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/C2F1728B-A4BE-E811-9077-001EC9ED8F2B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/464BCCF4-72BE-E811-BBA1-7CD30AC030A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/C892B97B-53BE-E811-A755-7CD30AC030A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/50907959-CABF-E811-B786-1CB72C1B6C4A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/7ED1E780-E3BF-E811-BBB9-1CB72C1B6C4A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/CCAB407B-99C0-E811-A76E-001E67E71408.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/AABB087E-5FBF-E811-8A68-E0071B741D70.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/2620C7D8-DDBF-E811-B146-E0071B6C9DB0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/6E6F59E2-A9C0-E811-AEE3-5065F3815241.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/5C4A00E8-B1C0-E811-88AE-008CFA197D98.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/50B84098-A2BE-E811-AE8E-002590E1E9B8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3E0CA6D5-86BE-E811-A0AA-0CC47AD98D08.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/E20DD6AA-86BE-E811-AF03-0CC47AD98F6A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3443962B-87BE-E811-A66C-0CC47A6C0716.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/6CCB1651-A3BE-E811-A8AD-1C6A7A26C57B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/34CB89BD-92BE-E811-B37A-0CC47A13D16E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/5A8D52AF-A4BE-E811-8740-44A8420CC916.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D0F859A3-95BE-E811-9DF7-D4AE52901F6A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/22B4892B-C5BF-E811-812C-F04DA2756D51.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D01350CD-F9BF-E811-80F2-7CD30AD0A7BC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/405654C4-D8BF-E811-9DD2-246E96D14AB0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/B64EC9D9-7AC0-E811-AB3D-14187763B811.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/5E682234-B5C0-E811-83FD-901B0E5427B0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/64D75337-77BE-E811-B608-6805CA02F25F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/907513A5-DDBF-E811-BFA3-0025905A6088.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/0C63B41E-D7BF-E811-8EFA-0025905B85B8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/6622CC07-C0C6-E811-BCCD-008CFA197444.root',
] )




































