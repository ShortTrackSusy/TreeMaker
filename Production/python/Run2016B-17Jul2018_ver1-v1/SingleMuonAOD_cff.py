import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/DCFF0B01-F07E-E711-802C-0CC47A4D765E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/2E80A6CD-F27E-E711-B6B7-0025905A6134.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/A2D9340A-F67E-E711-8B0E-0CC47A4C8F10.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/EEB9985E-F87E-E711-851B-0CC47A4D7662.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/ACF28144-FB7E-E711-B76B-0025905A6132.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/4EE89A41-FD7E-E711-961A-0CC47A4C8F2C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/3450AF48-FD7E-E711-9768-0CC47A4D767C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/E0F9D540-FC7E-E711-ABB2-0025905A6132.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/1AEAAF41-FC7E-E711-A322-003048FFD71C.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/DCFD8D43-FB7E-E711-BBAA-0025905B855C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F6779090-FE7E-E711-8A78-0CC47A7C3444.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/964CC794-FE7E-E711-B8F3-0CC47A7C347A.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/4E24D345-FD7E-E711-9BF0-0025905A60F2.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/7E108446-FD7E-E711-B49A-0025905A60BE.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/B0128C9A-FE7E-E711-86DF-0CC47A4D765E.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/5A97AD46-FD7E-E711-AF53-0025905A6136.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/12BA4CF7-FF7E-E711-A14E-0025905B8612.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C265D534-017F-E711-B4BE-0CC47A7C347A.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/0C296E9C-027F-E711-94C2-0025905A48D0.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F2655196-027F-E711-B36C-0CC47A7C3410.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F495C792-FE7E-E711-8774-003048FFD7A4.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/8E4352F6-FF7E-E711-A35E-0025905B861C.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/5444729E-027F-E711-AFF3-003048FFD722.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/02EB4D9B-027F-E711-9766-0025905A60D0.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/B867D292-FE7E-E711-9A4E-0025905B861C.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/DC59FAF8-FF7E-E711-9D8D-0025905B8582.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D858FB9A-027F-E711-BFFF-0025905A6134.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/EE29B485-047F-E711-906B-0CC47A4D7644.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C8F6491A-067F-E711-B238-0CC47A7C3410.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/38BED23B-017F-E711-943B-0025905B85E8.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/80BB703A-017F-E711-B9C0-0025905B859A.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D87B179D-027F-E711-BF8B-0025905A6056.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/8CC2A89D-027F-E711-8774-0025905AA9F0.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F86F0189-047F-E711-829C-003048FFD7A4.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/50CD8020-067F-E711-BD24-0CC47A4D765E.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/1CE2C79C-027F-E711-B97C-0025905A6056.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C81AB19C-027F-E711-9C4B-0025905A60F2.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/3A92039D-027F-E711-B5E1-0025905B8598.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/308B0F9D-027F-E711-9C1D-0025905A60F2.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C83A9D04-077F-E711-BFF5-0CC47A7C357E.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/94711F02-077F-E711-90AA-0CC47A4D7650.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/FE619A35-087F-E711-B398-0CC47A7C357E.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/E2B9628A-047F-E711-ADA5-0025905B8590.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D8AAD387-047F-E711-BB32-0025905A6092.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/9C305288-047F-E711-B70F-0025905B8612.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/867E489D-027F-E711-87FF-0025905AA9F0.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D4EE0C9D-027F-E711-B4EA-0025905B85DA.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/50F1699E-027F-E711-85B7-003048FFD722.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/3AA2349D-027F-E711-9416-0025905B85DA.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/BC21530A-077F-E711-BF83-0CC47A78A496.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C6E06E3C-097F-E711-BBED-0CC47A4C8F2C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/FE830741-097F-E711-9FD2-0025905B861C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C084373F-097F-E711-9FEB-0025905A48D6.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/DEC145D8-0B7F-E711-84FB-0CC47A4D7662.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/30CDBE95-047F-E711-B37A-0CC47A4D76AA.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/0AA7A521-067F-E711-8867-003048FFD722.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/00CADD20-067F-E711-94A4-0025905B859E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/82637720-067F-E711-BAC7-003048FFD75A.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/1C65280A-077F-E711-9633-0025905B85BC.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/446E1E80-0A7F-E711-9EE6-0CC47A4D75F6.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/A44ACD85-0A7F-E711-88C1-0CC47A4D7616.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/422CE23D-097F-E711-8A25-003048FFD7AA.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/FC1DBD3E-097F-E711-922C-0025905A48BA.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/FEA29F3E-097F-E711-A1B1-003048FFD79E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/80EBE922-067F-E711-9195-003048FFD7A4.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/14AF76C9-0C7F-E711-86CE-0CC47A4D75F2.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/BAA46C85-0A7F-E711-BFF5-0CC47A4D7692.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D87B513E-097F-E711-92EC-003048FFD75A.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/7E435FD9-0B7F-E711-BF79-0CC47A4D75F6.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/280B5941-FC7E-E711-B88B-0025905AA9CC.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/2C4C143A-087F-E711-A349-0025905A60B6.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/26F34639-087F-E711-A3BA-0025905B8582.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/3C2BC9C8-0C7F-E711-90A0-0CC47A4C8ECA.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/9A9014C9-0C7F-E711-A7AE-0CC47A4C8ECA.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/966F84C9-0C7F-E711-A19B-0CC47A7C357E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/3CB73CC9-0C7F-E711-AAFA-0CC47A4D7636.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/949E493F-097F-E711-8AD6-0025905B85DA.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/7E4435DF-0B7F-E711-B8B0-0025905A48F2.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/043A871E-0E7F-E711-B518-0025905A60BE.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/2EF40C1E-0E7F-E711-8DC6-0CC47A4D7692.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/80372EDD-0B7F-E711-8C08-0025905B8582.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/36961546-107F-E711-B279-0CC47A4D7636.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/2E693844-107F-E711-B0FB-0CC47A7C3430.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F490D1CF-0C7F-E711-9E86-0025905B85D2.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/A6C1B020-0E7F-E711-A3FF-0025905B8590.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/94DA2720-0E7F-E711-B3F9-0025905A60F2.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/6656B8E7-127F-E711-9388-0CC47A4D7674.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/7E2E5018-0F7F-E711-9A50-0025905B859E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/68D45B13-0F7F-E711-B9C7-0025905A60D6.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/FEEC0F10-0F7F-E711-BD73-0025905A48D0.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/E435A514-0F7F-E711-A723-0025905B855E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/0A31474B-107F-E711-B4A4-0025905A48D6.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/B0CA96EB-127F-E711-970A-0CC47A4D7618.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/AEA04FEB-127F-E711-AB43-0025905AA9F0.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/585852EB-127F-E711-B984-0CC47A4D763C.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/CC562018-0F7F-E711-AE5C-0025905A4964.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/206F7083-0A7F-E711-ABF8-0CC47A4D761A.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/EEEC7A08-077F-E711-BEC9-0CC47A4C8F0C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/ACA76CEC-127F-E711-82E7-0025905A6092.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/285D85ED-127F-E711-BBCB-0025905A6132.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/AC1787EE-127F-E711-9806-0025905A605E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/B669DE09-177F-E711-BCA4-0CC47A4D7674.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/5A39944E-177F-E711-ACA7-0025905B85B6.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F819E0DC-137F-E711-BE04-003048FFD71C.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/9EBCAE0D-177F-E711-91B0-0025905A6056.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/B825C49B-187F-E711-A99F-0CC47A78A41C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/64DECA6B-197F-E711-9B52-0CC47A78A42E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F0F51138-087F-E711-BEF0-0025905AA9CC.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/308FA610-177F-E711-A2C7-0025905B858E.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/FAFFE899-1A7F-E711-8E89-0CC47A4D75EC.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D687680F-177F-E711-8699-0025905A6134.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/5A87DE10-177F-E711-AA92-0025905A6132.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/64D0C30F-177F-E711-850E-0025905A60BE.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C0916A9F-187F-E711-A62A-0025905B85D8.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D2C0894F-177F-E711-8368-003048FFD71C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/AEBDB90F-177F-E711-888B-0025905B85DA.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C0587DA4-1B7F-E711-85F3-0CC47A4C8E2A.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/F450C2A6-1B7F-E711-8B09-0CC47A4D767E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/BE424687-0A7F-E711-A6B6-0CC47A4D761A.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/4A122E71-197F-E711-B1AE-0025905A60B8.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/8AFDFE4E-177F-E711-95E4-0025905B85DA.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/EE33DB14-177F-E711-8C97-0025905A48BC.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/4A1BDE9D-1A7F-E711-9274-0025905B859E.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/0A2D4F01-1F7F-E711-84B3-0CC47A4C8E98.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/CA00B613-177F-E711-9714-003048FFD75A.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/466F4033-1E7F-E711-B182-0CC47A7C347A.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/44D090A9-1B7F-E711-A92C-0025905A611C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/6278499C-187F-E711-9D21-0025905A60D0.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/80240204-1F7F-E711-A90B-0CC47A4D7628.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/40058B02-1F7F-E711-B0A3-0025905A48D6.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/9A70EB37-1E7F-E711-A214-003048FFD71C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/EC9F1D39-1E7F-E711-8F24-0025905B85C6.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D00C31E5-1C7F-E711-97AE-0025905A60B4.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/D09D2D05-1F7F-E711-A088-0CC47A4D7616.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/36313405-1F7F-E711-BBBA-0025905A60B8.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/7003EA36-217F-E711-B038-0CC47A4C8F2C.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/062D0C35-1E7F-E711-A632-0025905A60D0.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/DA6704A9-1B7F-E711-B908-0025905A6132.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/C4388D02-1F7F-E711-93C4-0025905A48D6.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/DA17FFC9-227F-E711-ACA3-0025905AA9F0.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/48EC1ECC-227F-E711-8CF0-0025905A605E.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/383F743A-217F-E711-AC5B-003048FF9ABC.root',
#'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/3C837ACC-227F-E711-B41D-003048FFD798.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/4A2C2C48-257F-E711-AD02-003048FF9ABC.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/B84E5B15-2F7F-E711-AF8D-0025905A611C.root',
'/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver1-v1/70000/4221947C-377F-E711-B388-003048FF9ABC.root',
] )













