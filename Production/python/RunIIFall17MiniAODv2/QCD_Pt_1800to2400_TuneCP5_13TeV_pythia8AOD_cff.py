import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D04988C7-B3D5-E711-A58D-0CC47A78A456.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F2EB9A2D-C7D5-E711-A9BE-0CC47A7C34A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/8C872638-9CD5-E711-B49A-0025905B856E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/9E8B8985-B7D5-E711-AA8A-0CC47A4C8F08.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1E5AFF5A-9BD5-E711-B1E3-0025905B85D6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/74BF4DE6-BAD5-E711-A082-0CC47A4D7674.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/CE4D153C-9CD5-E711-8373-0025905A6076.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/12A7D946-B7D5-E711-9667-0CC47A4D75EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1CCFE558-B2D5-E711-B728-0025905B8568.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/AC381BAC-B2D5-E711-A428-0CC47A7C35B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/74FE53DE-B4D5-E711-8F0B-0025905A6064.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D618D792-9CD5-E711-A7B7-0025905B858E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/08F32BD3-B4D5-E711-B82B-0025905B856C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1C9B4A36-C7D5-E711-A375-0CC47A4D760C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A0C16766-BBD5-E711-B1DD-0CC47A4C8EA8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3CC1FE8F-C3D5-E711-B1F0-0025905B85BA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0CE5C5C2-ADD5-E711-BD8A-0025905B85DC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/6841DA16-B0D5-E711-A6C1-0025905A48EC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C2A5BE70-C7D5-E711-BFA0-0CC47A7C3450.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D2CA54FB-ADD5-E711-BFF1-0025905B8586.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/74824AD2-C3D5-E711-A7DC-0025905B8592.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D25FC310-AED5-E711-8081-0025905B855C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A4902DF7-C3D5-E711-BA74-0CC47A7C3408.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/8C55AD26-B3D5-E711-8CD8-0025905B858E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/62841338-E6D5-E711-95A3-0CC47A78A4A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D8476B8D-C3D5-E711-8B2B-0CC47A7C3408.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E8E017B3-DED5-E711-8AA4-0CC47A4C8E82.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/06A076E1-7ED5-E711-8011-0CC47A7C3408.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DA3745A9-4AD5-E711-9B5B-0025905B858A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/44A9FD23-3CD5-E711-AD20-0CC47A4C8F08.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/964B92C6-51D5-E711-9799-0025905B85AA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE5D1A4E-81D5-E711-9133-0CC47A4C8F12.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D64A25CA-80D5-E711-9CF1-0025905B857C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/08FEC9D3-5BD5-E711-A666-0025905A609A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4AD9BA08-87D5-E711-AC1F-0CC47A4D7692.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FC644D10-82D5-E711-9245-0025905A6138.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/5CCAD866-53D5-E711-83D3-0025905A60DA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F4CA5200-7FD5-E711-9A12-0025905A60A6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/02BE9F51-6CD5-E711-A7C4-0CC47A7C3428.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C0570110-81D5-E711-B11C-0025905A6064.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/CEADFBD1-5BD5-E711-9304-0025905A6084.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/044BE7A1-81D5-E711-AC43-0CC47A4C8E16.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/949D52AD-87D5-E711-8C25-0CC47A7C34C8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/20FBE62B-81D5-E711-B908-0025905A60FE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/264D9AEB-88D5-E711-82C1-0CC47A4C8EBA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/8E3F0CB2-87D5-E711-990B-0CC47A4C8E1C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/609DC41F-82D5-E711-AF92-0CC47A7C35F4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/8A7C4F59-C3D5-E711-8964-0CC47A4C8EB6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E086ED82-87D5-E711-8839-0CC47A4D76A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F412AD37-87D5-E711-B0EA-0CC47A4D7654.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/7204F025-C3D5-E711-BAE0-0CC47A4D76C0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FA253031-9CD5-E711-8A0E-0CC47A7C3422.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/CCF627E1-BAD5-E711-B9F3-0025905B8610.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/50AC805F-3CD5-E711-99EE-0CC47A4C8E86.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/AACD1976-89D5-E711-880B-0CC47A4D7646.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/420B5079-BBD5-E711-9A17-0CC47A78A496.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B2F6E458-AFD5-E711-9A34-0025905A6082.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A86CD6D7-C3D5-E711-BC41-0CC47A4D75F2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1069CAFC-AFD5-E711-9DEE-0025905B8582.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C612C3EF-C3D5-E711-9972-0025905A6070.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/203274E0-B2D5-E711-BE5A-0025905B85F6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4ABA3E54-B3D5-E711-873C-0025905A608A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/66D55528-AFD5-E711-BD20-0025905A612C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/54F39A9D-B6D5-E711-BE0D-0025905A60DA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/047810CF-B2D5-E711-A77D-0025905A6092.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/668576AB-DDD5-E711-A63C-0CC47A7C34C8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C420647C-B7D5-E711-AB67-0025905A6138.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1E02B113-BBD5-E711-A372-0025905B860C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E018CD65-B5D5-E711-BA60-0025905B861C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/9C422017-CBD5-E711-9DBA-0CC47A4D768E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/34B422A1-B2D5-E711-904B-0025905B857A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A06BDFBB-CBD5-E711-A224-0CC47A7C3612.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/24E11FB2-D7D5-E711-8945-0CC47A7C354A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/02E38DD2-D7D5-E711-B4C0-0CC47A7C35F4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4A449688-BBD5-E711-A370-0025905B85AE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DC9D5881-ECD5-E711-8A1B-0CC47A78A2F6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/261A2336-BBD5-E711-B042-0025905B858A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0479EA63-BBD5-E711-91E1-0025905A48D8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/18993115-CBD5-E711-B260-0025905B8562.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/9067FB80-C7D5-E711-BA5F-0025905A607E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/7CD331ED-E0D5-E711-B382-0CC47A7C35F4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0207EC3C-EBD5-E711-89AB-0CC47A7C3604.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/06B32E06-21D5-E711-93E4-0CC47A78A496.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B28B5FC2-4AD5-E711-ADFD-003048FFD76C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F672F56A-31D5-E711-8291-0025905A60DA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/2276E1BF-57D5-E711-9C7E-0CC47A7C35E0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/86F878CF-33D5-E711-94CF-0CC47A7452D0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D222D1C5-4BD5-E711-8450-0CC47A4D765E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0E0E3BFA-44D5-E711-BAEF-0CC47A4C8E2A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/56F17DFA-1CD5-E711-AE35-0025905A6110.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E2A6C35E-18D5-E711-A5DB-0CC47A4D75F2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE19EA03-45D5-E711-BB56-0CC47A78A4B8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/8AB06879-33D5-E711-A510-0CC47A4D768E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/804D9078-24D5-E711-BC32-0CC47A7C3408.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/22EAAF27-35D5-E711-96BB-0CC47A4D7654.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0C51530E-32D5-E711-B550-0CC47A4C8EBA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/741B923D-1ED5-E711-A919-0025905B8592.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/402BD90D-35D5-E711-9C12-0CC47A4D75F6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3E35C769-51D5-E711-972F-0025905A48F2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/BC076E9C-4AD5-E711-9BC7-0CC47A4D76B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/AE2417ED-4BD5-E711-9979-0CC47A7C35C8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B892DD9B-4AD5-E711-91D7-0CC47A7C35D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/403AEC2B-3BD5-E711-8F90-0025905A48D6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/6253D86A-ACD5-E711-A00E-0CC47A4C8E34.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/023BDF16-40D5-E711-9272-0025905A612E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/982EBE69-ACD5-E711-A01C-0025905A60CA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/724DEBB6-ACD5-E711-B984-0025905A48F0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/84987825-45D5-E711-95EF-0025905B85D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/7211BF4A-63D5-E711-9ECD-0CC47A4C8E38.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/BEAEB26F-A2D5-E711-B26A-0CC47A4D76CC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C89CB361-80D5-E711-BFB5-0025905B85C6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/AEF458BD-9BD5-E711-900B-0CC47A4D762A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0682268F-E4D5-E711-A364-0CC47A7C356A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/AEEB05A7-81D5-E711-A793-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/74CFDF9B-81D5-E711-A8DB-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/04D63591-81D5-E711-A96A-0025905A48FC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/80C495E2-7ED5-E711-A188-0025905A497A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E8E15409-82D5-E711-ADC6-0025905B859A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3E9EBB08-82D5-E711-980F-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FA1CF73F-9DD5-E711-B966-0CC47A78A4A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D0D21EA8-81D5-E711-800A-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DECE81C0-BAD5-E711-A957-0CC47A7C3604.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/6EBE0328-9DD5-E711-BF17-0CC47A4D7674.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/30BBF458-B7D5-E711-B6ED-0CC47A7C347E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/404C7017-82D5-E711-A07D-0025905A610C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/72FFF13A-9DD5-E711-AE62-0CC47A4C8E98.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DCC058F9-A1D5-E711-A77B-0CC47A4D767A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1AF91414-82D5-E711-ACFA-0025905A6126.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3A759101-9AD5-E711-AE4B-0CC47A4D765E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C8E726C5-9AD5-E711-9853-0CC47A7C3428.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E65D46D5-9AD5-E711-8156-0CC47A78A496.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/065BDC9F-81D5-E711-B830-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4C7353BF-9BD5-E711-A9CC-0CC47A4C8E86.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B8E4E59B-81D5-E711-8DF5-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3A27AF86-81D5-E711-9D28-0025905B85A2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/389BC09A-99D5-E711-888B-0CC47A4C8E22.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3A688328-9DD5-E711-85D8-0CC47A7C35A8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/EABBEC3A-1ED5-E711-967D-0025905A60B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/68B71070-82D5-E711-BD1B-0025905B8574.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/34440B13-82D5-E711-85DA-0025905A6104.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/AC5F0132-9DD5-E711-91CF-0CC47A78A436.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE0668ED-9AD5-E711-8CCA-0CC47A4D7646.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/921DF50F-82D5-E711-AF49-0025905A60B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/2255740E-9CD5-E711-8714-0CC47A7C345E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/640A3293-B7D5-E711-A767-0025905B8572.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/56443A9F-81D5-E711-A3BD-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B63DB994-81D5-E711-9B08-0025905A48B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/40C7CA4A-B5D5-E711-AF70-0CC47A7C340E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/7A3BDD86-9AD5-E711-B12A-0CC47A4D76AC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/028E905B-C4D5-E711-8116-0CC47A4C8F0C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/76C190E5-BAD5-E711-9947-002618FDA265.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/1C66CB23-A2D5-E711-BCB6-0CC47A7C35D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/BEE7653C-99D5-E711-B114-0025905B8596.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/2482D919-BBD5-E711-9081-0CC47A7C3404.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/9000972B-A2D5-E711-A192-0CC47A7C3434.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/BE55B422-B5D5-E711-9C9D-0CC47A4D767A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D0778732-B2D5-E711-919A-0CC47A7C3610.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A4C5E56C-A2D5-E711-BF74-0CC47A4D76AC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/960711F1-B4D5-E711-A677-0CC47A7C3408.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C45C25C5-B2D5-E711-A3F7-0CC47A4C8E38.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B6B7966B-B2D5-E711-A5BB-0CC47A4C8E14.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D042283F-B2D5-E711-A415-0025905B85D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/6EF9F823-99D5-E711-8490-0025905B85D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/62EDEDFA-C6D5-E711-815A-0CC47A78A340.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4006CDD5-B6D5-E711-B84D-0CC47A4C8E66.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/38FD2CA1-E6D6-E711-982B-0025905A60A6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/4E73E90A-0CD7-E711-88AB-0CC47A7C35D8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/36700391-E6D6-E711-AC19-0025905A6104.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/00CC5A51-35D7-E711-B69D-0CC47A4C8ECA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/82A6D17F-0BD7-E711-9697-0CC47A7C346E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1614D224-23D7-E711-9139-0CC47A4D769A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/32CFB825-23D7-E711-AD20-0025905B85BC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/08CD79E5-37D7-E711-8B55-0CC47A74527A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/445C6A2F-4BD7-E711-9633-0CC47A4C8ED8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/207B4501-44D7-E711-A083-0CC47A4C8E2E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/38ED7D85-57D7-E711-B0CB-0CC47A4D7650.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D6E43B2C-49D7-E711-9F1F-0025905B85D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/86F0D7E8-57D7-E711-A9F4-0025905A60C6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/647D17D5-57D7-E711-862F-0CC47A4D765E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/24F4CE13-20D8-E711-B2B2-0CC47A7452D8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/5291D066-28D8-E711-A59C-0025905A48F0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/46C2DB63-28D8-E711-9EBC-0025905A60B4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DAAD4FD9-86D9-E711-ADFE-0CC47A4C8E2E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4ECAE1FE-7CD7-E711-AAC2-0025905B8564.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/72F89065-0BD7-E711-8415-0CC47A4C8F0C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/28408A12-EAD6-E711-B181-0025905A60E4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C29C14F3-C3D7-E711-BD4E-0CC47A7C357E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/28F660F9-EFD5-E711-967B-0CC47A78A496.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/3087E382-EBD5-E711-ACB9-0CC47A4D7674.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/8421491B-E6D5-E711-BFF8-0CC47A4D762A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E4C239DF-CBD5-E711-9A90-0025905B8564.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/2ECC83E9-ECD5-E711-8F59-0CC47A4D7650.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E2CD047A-CBD5-E711-BF48-0025905A60AA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/228FE109-C7D5-E711-9B38-0025905B855E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4243E154-CBD5-E711-AB74-0025905B8592.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A2B5DCA9-CBD5-E711-AECE-0025905B8598.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/5E9220DD-CAD5-E711-8329-0025905A6070.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DE088473-CBD5-E711-AB40-0025905B8604.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/2E1DBE2F-E9D5-E711-A069-0CC47A4D76A2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FCF30858-F4D5-E711-B7C8-0CC47A4C8F26.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/9A463097-BBD5-E711-95A0-0025905B85AA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0EEB87E6-D8D5-E711-A8C3-0025905A48D6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/961CD9C3-EBD5-E711-AF60-0CC47A4C8E28.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0C869E3A-E9D5-E711-B76D-0CC47A78A4A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/BA622A8A-19D6-E711-B202-0CC47A4D7646.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/067ADE55-EBD5-E711-BED2-0CC47A4D7678.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0497545D-11D6-E711-ACAA-0CC47A4D7654.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/00B438F2-DED5-E711-A7BA-003048FFD7AA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F45123E2-EFD5-E711-A440-0CC47A74527A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/0CFC0DEA-E0D5-E711-9ABA-0025905A6056.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B21B01BC-ECD5-E711-BF55-003048FFCBB2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E25FE9C4-E6D5-E711-BEFF-0CC47A78A478.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/64EE1083-EBD5-E711-82A4-0CC47A78A4B0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/7AD80F62-17D6-E711-A7E5-0CC47A4D760A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/347068CB-E5D5-E711-8814-0025905B85C6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/020133ED-81D5-E711-91B1-0CC47A7C3434.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F06AEC38-10D6-E711-92A3-0CC47A78A456.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4A6288CD-F2D5-E711-95A5-0025905B85EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/4AAABD62-F4D5-E711-9E73-0025905A6104.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E6E07E5D-10D6-E711-906D-0025905A4964.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C013EA6A-17D6-E711-9EB2-0CC47A4D75F2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/363A67D9-11D6-E711-B70F-0025905A6080.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/DE0B763D-11D6-E711-85DA-0CC47A4D76D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/244E376F-EBD5-E711-BF4A-0CC47A745284.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/72D800DE-F3D5-E711-9A71-0CC47A78A4B8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/12BC31D0-F7D5-E711-B5F6-0025905B8572.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/BC50DAD2-E5D5-E711-9FD6-0CC47A4D760C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/5A8219D0-F2D5-E711-A36B-0025905B85CC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/786D345A-81D5-E711-B676-0CC47A4D7638.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/D0F4B0E5-F3D5-E711-8E44-0025905B85FE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE4156CE-E5D5-E711-ADCA-0CC47A7C3434.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B856F958-11D6-E711-9C0D-0025905B8594.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/52A4CBA6-E6D5-E711-8AD4-0025905B859E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/22BC4EBB-52D6-E711-B1AE-0CC47A4D769A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/24E69D8D-19D6-E711-A8D7-0025905B8576.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/823C0A9C-81D5-E711-AC71-0025905A48FC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/76495361-C7D5-E711-BFBE-0CC47A4D76A2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/C2F66E20-80D5-E711-A27A-0025905B861C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/E6D51BBF-53D6-E711-96C0-0025905A60CE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/F8B96AFF-96D6-E711-93A5-0025905A6122.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/A6AB727A-B0D6-E711-954E-0025905A60CA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/84544B54-D6D6-E711-8D72-003048FFD72C.root',
] )













