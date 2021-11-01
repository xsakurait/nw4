データ水増し
　画像に変形、エフェクトをかけ画像枚数を増やし機械学習を向上させる
なぜ？
　機械学習とは各画像から共通点を見つける
　多くの画像から学習することで正しい共通点を学習する可能性が上がるから

画像にノイズを乗せることで環境変化に対して強くなる

画像の変形エフェクトの事例
　コントラスト修正、反転、４5度回転、ノイズ
　グレイスケール、フィルタ、切り抜き
なぜ４５度回転なのか？

３次元の画像を学習して２次元の画像をモデルに入力した場合、
正しい結果が得られるのか？

imageJではpythonやExcelを使わなくてもマクロ作成を行える
ただしimageJだけの操作だけと感じたので、やはりpythonの自動化の分野は学びたいと感じた
photoshopなどとは違い無料なので使いたいと感じた

マクロのやり方
imageJ開く
pluginsでMacro record 
imageJで操作する
マクロのウィンドウに操作のソースコード書いてあるので、コピーする
plugins>New>Macroでそこにペースト

inputdir = getDirectory("One above the image directory");// ディレクトリを指定
dirlist = getFileList(inputdir);//画像ファイルを配列取得
for(i=0;i<dirlist.length;i++){
    inputdir2 = inputdir + dirlist[i];
    filelist = getFileList(inputdir2);
    for(k=0;k<filelist.length;k++){
        print(filelist[k]);
        openfile = inputdir2 + filelist[k];
        open(openfile);
        //Add Noise
        run("Add Noise");
        saveAs("Jpeg", openfile + "-Noise");
        close();
    }
}
ディレクトリかの画像データを全てにノイズ追加し、
それを同ディレクトリの階層に保存

作りたいアプリ　数次判定する
見たノートが何の数字かわからないことが多々あるから
客観的な意見、つまり答え合わせが欲しいから。