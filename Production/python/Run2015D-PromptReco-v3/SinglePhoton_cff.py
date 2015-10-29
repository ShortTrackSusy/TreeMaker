import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/584/00000/AE89EEAF-855D-E511-9B3B-02163E013592.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/587/00000/9281243A-945D-E511-96EF-02163E011FBB.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/629/00000/3C869B3B-115F-E511-AB40-02163E0146D2.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/630/00000/BE4748B0-295F-E511-A271-02163E014402.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/662/00000/A24157CC-075F-E511-89E9-02163E013458.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/672/00000/E4C5C3DF-025F-E511-997E-02163E013918.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/673/00000/7C000AF7-225F-E511-BE0C-02163E0145CB.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/674/00000/E253BB08-065F-E511-8CD9-02163E011BE4.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/675/00000/6EA59418-B25F-E511-A0E7-02163E01371D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/675/00000/DEEB4718-B25F-E511-914A-02163E011A8A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/0A062686-AC5F-E511-84C8-02163E011FAC.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/42BA7A81-AC5F-E511-B616-02163E011A8A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/48A7748A-AC5F-E511-AF81-02163E0144C7.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/48E36F80-AC5F-E511-B938-02163E0143E2.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/66CA398E-AC5F-E511-A0A3-02163E01431C.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/A404177F-AC5F-E511-9753-02163E013411.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/DCFF7489-AC5F-E511-88F8-02163E01393E.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/677/00000/4031592C-275F-E511-9187-02163E0141D6.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/677/00000/80F90E1E-275F-E511-831C-02163E01474F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/677/00000/D0AEFD42-275F-E511-B80B-02163E01443C.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/721/00000/D89CF3C6-075F-E511-9810-02163E014504.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/725/00000/040FBC97-395F-E511-9CA8-02163E0136E3.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/727/00000/4884FAD6-435F-E511-9476-02163E0144BA.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/728/00000/8C18777C-3A5F-E511-BD8C-02163E013390.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/12C1D1E8-3E60-E511-981E-02163E011C91.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/2A6652EC-3E60-E511-8619-02163E014734.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/2C16C805-3F60-E511-A4C5-02163E012096.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/44331506-3F60-E511-8DE2-02163E01475F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/482403E7-3E60-E511-BCA2-02163E011FEF.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/7699BEE7-3E60-E511-9D68-02163E0139E0.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/84144104-3F60-E511-97DF-02163E012A7D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/920AD7EC-3E60-E511-A5DA-02163E012434.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/DE0B41EA-3E60-E511-ADC6-02163E01352A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/734/00000/DA6FF6AD-E85F-E511-A08B-02163E012753.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/734/00000/E28307AE-E85F-E511-8AC6-02163E01210D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/798/00000/7245B4EB-B15F-E511-91C0-02163E0128A8.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/801/00000/308FD73F-7860-E511-A85C-02163E011B36.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/801/00000/38C6B036-7860-E511-811B-02163E01463F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/834/00000/DCD553A3-0060-E511-A6F1-02163E011A43.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/842/00000/C6A64E67-6360-E511-83B9-02163E014792.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/3617D848-1261-E511-A035-02163E011F62.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/54F4655B-1261-E511-85E6-02163E014567.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/566BDA54-1261-E511-8D4A-02163E014219.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/6E3F7979-1261-E511-972A-02163E011D35.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/78D34645-1261-E511-AF2B-02163E0146B5.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/7E98D061-1461-E511-ABAF-02163E01475D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/843/00000/96E5554C-1261-E511-8B06-02163E011B5E.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/865/00000/9C60DFF7-ED60-E511-9ADB-02163E0128CE.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/866/00000/8487A89D-FC60-E511-A52B-02163E016F51.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/867/00000/6C9D42C7-1C61-E511-B24A-02163E011C7B.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/868/00000/1C77C74E-9561-E511-99DF-02163E013520.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/868/00000/429A0B3A-9561-E511-B8DC-02163E013559.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/868/00000/4402D344-9561-E511-AB3D-02163E01436A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/868/00000/5C4E379F-9561-E511-A6FD-02163E0144BE.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/869/00000/7034AF15-1761-E511-A997-02163E011864.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/924/00000/A0DF0870-6961-E511-A86B-02163E0141DA.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/925/00000/4C5EB52E-6A61-E511-A9C4-02163E014542.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/926/00000/E86016E8-1967-E511-8905-02163E012607.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/935/00000/40DCFE17-9D61-E511-962C-02163E014262.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/936/00000/1E54B582-1662-E511-AD02-02163E014407.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/936/00000/24E6928A-1662-E511-840F-02163E014131.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/936/00000/30F91881-1662-E511-B3E2-02163E014362.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/936/00000/5AC36586-1662-E511-A888-02163E0145B2.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/936/00000/D8667988-1662-E511-9E94-02163E013775.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/936/00000/DC55BF8B-1662-E511-A3FA-02163E01445A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/941/00000/560D7021-1C62-E511-A1E6-02163E0136FD.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/941/00000/8E960DCC-1C62-E511-B71C-02163E014725.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/024/00000/4EFD01A8-2562-E511-AA63-02163E013436.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/027/00000/F0C0D219-3262-E511-9C4F-02163E01448B.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/394/00000/D0293889-1C64-E511-8E14-02163E013470.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/395/00000/A28C320F-2664-E511-B492-02163E0140D6.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/396/00000/6A4FF870-1365-E511-9AE3-02163E01432A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/397/00000/1A8E3405-5564-E511-869E-02163E0140EE.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/398/00000/2EDAF0B7-2B64-E511-87FB-02163E01458E.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/399/00000/2CCB437B-6764-E511-AB4A-02163E014113.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/399/00000/AEF54928-6764-E511-9DA9-02163E012027.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/08E5B2BF-2665-E511-96F5-02163E01395C.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/105E51B4-2665-E511-847D-02163E01410F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/186C0FB3-2665-E511-9FD1-02163E01376A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/620306D6-2665-E511-9A33-02163E0142FB.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/9ED41761-2765-E511-B3D5-02163E0140F7.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/9EDF0BC2-2665-E511-B21A-02163E0145E3.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/D2ECA7B7-2665-E511-9A75-02163E01475E.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/400/00000/D4CF04B2-2665-E511-83A3-02163E0138D6.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/460/00000/0260651B-DB64-E511-9773-02163E01261A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/461/00000/A2CC0698-AF65-E511-89A5-02163E013731.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/461/00000/BE5CB945-BC65-E511-B0CE-02163E014414.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/487/00000/8ADFA1F7-3B66-E511-B01D-02163E014781.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/487/00000/A2ABF837-4366-E511-88D7-02163E0118AD.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/487/00000/B0631682-4266-E511-B826-02163E0138E6.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/490/00000/34340B34-4766-E511-89DC-02163E0119EE.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/529/00000/84A1814E-D165-E511-B789-02163E011C4C.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/531/00000/30E2C798-FE65-E511-940E-02163E013858.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/531/00000/743AC13F-FE65-E511-90CF-02163E013532.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/598/00000/2E391970-2B66-E511-9603-02163E0125E5.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/599/00000/06B85507-6066-E511-8DE4-02163E014246.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/599/00000/8C0136D4-6066-E511-80A6-02163E011C42.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/611/00000/B4E63A04-6566-E511-A4CC-02163E0145DF.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/257/644/00000/5C423529-1467-E511-AF24-02163E0144CE.root' ] );


secFiles.extend( [
               ] )
