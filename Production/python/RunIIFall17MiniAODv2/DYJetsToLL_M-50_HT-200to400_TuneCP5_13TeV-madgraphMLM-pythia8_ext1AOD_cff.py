import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D2FABD90-701B-E811-988F-0CC47AA477B6.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/26D15649-721B-E811-908C-0CC47A57CD00.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/66E992E3-891B-E811-8FD2-0025901AC12A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/3E3E25F2-891B-E811-A838-0CC47A0AD476.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/2E85C3DE-171C-E811-BB8D-002590D9D84A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D09E1C3F-1B1C-E811-A761-0025901ABD18.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/388F4AD9-501B-E811-9D19-24BE05C60641.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/DA4ECFA4-671B-E811-B1E8-5065F382A241.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/8AC327E9-5F1B-E811-9351-24BE05CEECD1.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/F807A362-861B-E811-87D0-24BE05CE0E41.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/DA430C49-691B-E811-A229-E0071B6CAD10.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/C4DCE24F-861B-E811-A29B-24BE05C63741.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/9408F935-701B-E811-A28D-24BE05C3DB21.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/FCC80110-6F1B-E811-9F38-E0071B74AC10.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/FC212452-CF1B-E811-A32F-24BE05C49891.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/3A4724EC-C21B-E811-89B6-E0071B7AF7C0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D023E0AE-4A1B-E811-97BE-008CFAE45248.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/9E8725D4-261B-E811-9291-0025905A6122.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/EE51C39E-261B-E811-BA60-0CC47A7C3434.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/F871440F-241B-E811-B622-0CC47A4D7650.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/8E2FA31B-241B-E811-BA13-0CC47A4D7674.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/1C04A128-7F1B-E811-93C8-0CC47A7C3636.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/CEB5ABD0-861B-E811-9C32-0CC47A4D7650.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/ACD76050-7F1B-E811-8E02-0CC47A4D768E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/34FD4748-7F1B-E811-89F4-0CC47A7C3638.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/B886C5A6-9A1B-E811-A8BC-0CC47A7AB7A0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/B297FDEF-861B-E811-BC3E-0CC47A7452D8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/FAC2477B-5C1B-E811-B1FA-008CFAC93D8C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/34BECF79-501B-E811-99FD-0025904A891A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/F4D6F88E-5C1B-E811-BE33-008CFAC91964.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/84549C7D-711B-E811-86F5-008CFAE451EC.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/9E2D3C60-741B-E811-AEFD-0025904AFFCC.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/3036129F-741B-E811-B50E-008CFAC8CD50.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/6A92B125-771B-E811-A29C-008CFAC93BF8.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/10435B62-161C-E811-B090-008CFAC91CAC.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/36B08AA3-9A1B-E811-AED9-0CC47A78A4A0.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/90B9811E-C51B-E811-8DAA-0CC47A74527A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/F4BF697A-DA1B-E811-BBDF-0CC47A78A4B8.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/B205DBEF-C21B-E811-B18E-0CC47A78A456.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/0AC14C05-FB1B-E811-96ED-0CC47A74527A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/2CE7CC62-161C-E811-BD30-0CC47A78A4B8.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/80866B06-131C-E811-8792-0025905B8580.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/E43EB0ED-AB1C-E811-A86A-0CC47A4D7678.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/7AD575A3-191B-E811-9A5A-1866DA85D853.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/DEDFA4D9-181B-E811-87BF-FA163E7A5F1C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/BE9C6518-951B-E811-B9D9-02163E019FD0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/7CD68FB9-951B-E811-9CBC-02163E01617D.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/508D519C-3D1C-E811-AA2A-FA163E7BC23F.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D8C0492D-301C-E811-906B-FA163EE65283.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D46ACC09-2B1C-E811-8DDE-FA163ECE3FC4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/747A86BE-2A1C-E811-9FC0-FA163EB8A649.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/E4122B6F-311C-E811-87FB-FA163EF9728B.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/3A9C1A81-641C-E811-A9F7-FA163E4B6F1D.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/A23DBBF0-181C-E811-AEC1-FA163EDA0FB2.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/34FF1E92-651C-E811-B3C3-FA163E6A0844.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/E246CBB0-C31B-E811-8BF7-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/70CEB40F-C01B-E811-8822-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/4A6E9F2D-B61B-E811-BCC7-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/44274164-B71B-E811-B431-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/5AF3AC00-C81B-E811-90F8-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/12E21312-8A1C-E811-91AD-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/7EABB033-061B-E811-B92A-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D0276021-361B-E811-BFCF-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/7261E77C-361B-E811-9839-0242AC130002.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/A418E5BA-611B-E811-A79B-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/FC583786-061B-E811-98F1-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/3EDA9B12-2A1B-E811-95C6-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/02D43C62-171B-E811-A299-0CC47A13D418.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/88E9BD0A-2A1B-E811-A276-002590E2DDC8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/F094F0EE-451B-E811-985D-002590E39D90.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/80C56AF3-471B-E811-8928-90B11C2CB7A9.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/E2AE1FF8-8D1B-E811-BFAD-0CC47A2AED04.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/465292D0-901B-E811-A825-0CC47A2B0744.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/DCAD69E9-F41B-E811-8240-0CC47A6C1806.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/8C7AE472-DD1B-E811-8E3C-0CC47AA992B0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/3CE4747F-1C1C-E811-899F-0CC47AD98BEE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/04B07050-F81B-E811-AC25-0CC47A13D418.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/A0CDB801-1D1C-E811-B398-0025901D08B6.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/B4236AB4-CB1C-E811-975F-0CC47AA992AC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/00196D9F-E81B-E811-94D3-141877638F39.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/1C1D9EE2-B71C-E811-B2C6-44A84224053C.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/382B801A-8D1C-E811-8651-00259021A53E.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/EEB52700-D31C-E811-89B5-001E675825D4.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/B22E55AD-6B1C-E811-9DBE-A0369FC5ED30.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/966B0F19-E71D-E811-AFBA-0025905C3E38.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/20863A98-CE1E-E811-84EB-0025905C53B0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/EA175E45-2C1C-E811-AE88-C4346BC8F6D0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/92D7D1BE-2C1C-E811-B4DF-AC1F6B1AF140.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/5469702D-8A1C-E811-9973-002590E7E050.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/6C02A87B-851C-E811-8515-44A842CFD65A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/E2652AFB-811C-E811-B8D0-001F29087E7C.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/605F17CB-891C-E811-BA65-0242AC1C0502.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/207D9C82-881C-E811-9DAC-0242AC1C0501.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/4A90A698-AD1C-E811-B537-A0369FC52350.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/2878D2F4-031E-E811-B764-A0369FD1EF00.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/6CC8888D-951C-E811-9E7E-38EAA78E2C94.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/4825FEBF-961C-E811-B800-38EAA78D8AF4.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/6EF5F95B-C21C-E811-A313-38EAA78E2C94.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/D29F41FD-881D-E811-A798-984BE164D07A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/EA69AAE8-E31D-E811-A7FF-90E2BAC9B7A8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/0EB2D786-741E-E811-B44B-44A842CFD5D8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/F47B636A-471D-E811-9519-0CC47A5FA211.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/AC50EB75-CB1E-E811-88F6-3C4A92F7DD0C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/CA8D71D8-F51E-E811-96E2-001E67580724.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/8230F3F5-CE1E-E811-82C9-002590DE6DE4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/CEB88200-CF1E-E811-AB44-F04DA27540C4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/0AB9AAAF-5D1D-E811-B4AE-FA163EF28A5C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/30903BC2-5D1D-E811-8D3D-FA163E946B87.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/2650D00E-E41D-E811-B43B-FA163EB3E2E8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/90267DEF-ED1D-E811-8064-FA163E7CF739.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/00000/928E5A79-BC1E-E811-BF9C-EC0D9A04AE30.root',
] )




































