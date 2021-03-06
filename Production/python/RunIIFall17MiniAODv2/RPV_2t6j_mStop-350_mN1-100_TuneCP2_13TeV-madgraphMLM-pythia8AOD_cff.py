import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/44F97D02-79C0-E811-A44D-509A4C74D07B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/52B32BF0-A6C0-E811-8EAF-509A4C74908E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/E8B92722-A5C0-E811-AA7A-008CFAF0842A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/A21F3AD8-99C0-E811-A893-F04DA275BFB9.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/9875816E-00C2-E811-AB52-008CFAFBE7DE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/FCA11FF6-6ABF-E811-AD22-5065F3819241.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/EAA6CF4A-E6BF-E811-B013-24BE05C63681.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/6EF6E484-68C0-E811-B258-E0071B7B2350.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/E03DD400-4ABF-E811-B6B0-0CC47AD98F74.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/B643D9B1-49BF-E811-A237-0CC47A13D216.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/8E85F2AB-E9BF-E811-8036-0CC47AD99062.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/DA874CA7-F0BF-E811-9C08-008CFAC93DA4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/F887B9B1-A6BF-E811-BEF8-0CC47A4D7666.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/A06190CB-D9BF-E811-B826-0CC47A4D7666.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/C6408F75-63BF-E811-8868-44A842129246.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/E8E3EC75-63BF-E811-B275-F01FAFE5D12A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/645294C0-E0BF-E811-8865-90B11C444042.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/304E5535-5CBF-E811-9ED8-3417EBE64426.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/C68EDE1B-61BF-E811-92C7-509A4C730E30.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D82866E8-56BF-E811-9BD1-3417EBE64B4F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/FA8AD12C-22C0-E811-BD5B-008CFAFBDBA8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/386FFE4D-7AC0-E811-9799-008CFAF3543C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/2464C476-64C0-E811-B724-509A4C858ADC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/52F5906C-56C0-E811-896E-008CFAF7174A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/687AA26F-6AC0-E811-8768-509A4C748128.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/04D5F4F5-7CC0-E811-97EF-7CD30ACE1732.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/6CC9ECD2-87C0-E811-91ED-3417EBE34B01.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3C080FB0-65C0-E811-A2B0-3417EBE34B01.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/4E0BCCB8-31BF-E811-9318-001E67DFF67C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/2443C6D2-32BF-E811-9D3F-A4BF01027688.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3CAD9F8E-CABF-E811-AEFB-EC0D9A0B33A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/FE3FDCEA-5EC0-E811-A21C-001E67E68BBD.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/DA064F40-ECC2-E811-A5AC-509A4C84547F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/74B6A8E4-94C3-E811-94FB-509A4C84EACC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/FAE28DD7-E7C7-E811-841B-0CC47AD98BC2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3E1D0B91-1AC7-E811-9C6A-90E6BA3BD76E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/4E2D6409-0AC8-E811-998B-008CFAF292B0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/AE42B652-95C7-E811-B254-0CC47AF9B2EA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/DC3B1EDE-B0C8-E811-B825-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/244739E5-19C7-E811-B983-B083FECFF296.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/36443A00-67C7-E811-AB8F-14187741121F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/CC6C91C1-67C7-E811-90A1-1866DAEA6D08.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/0A73D649-8CC8-E811-BD61-509A4C70AB6E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D6B21C6A-E0CA-E811-B276-34E6D7E3879B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/7058E4A4-D4D0-E811-8B0A-008CFA16615C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/089D83AD-A0D0-E811-9254-008CFA1111D4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/024F0CAB-A0D0-E811-A8FB-008CFA197444.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/924EB4AF-A0D0-E811-BC44-008CFA197954.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/56C9C9AB-A0D0-E811-B500-008CFA1111D0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3C1BF7AA-A0D0-E811-A40B-008CFA1974E4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/32F30FB0-A0D0-E811-8579-008CFA197DE4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/F0325FAE-A0D0-E811-88CF-008CFA1111D0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/66B7C5AC-A0D0-E811-8C05-008CFA197A28.root',
] )




































