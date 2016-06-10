# -*- coding: utf-8 -*-
import sys
import os
import os.path

def listup(srcRoot, destRoot, oldRoot, relativePath):

    srcPath = os.path.join(srcRoot, relativePath)
    destPath = os.path.join(destRoot, relativePath)

#    System::String ^ srcPath = System::IO::Path::Combine(srcRoot, relativePath);

#    array < System::String ^ > ^ srcDirItems = System::IO::Directory::GetDirectories(srcPath);
    items =  os.listdir(srcPath)
    dir_list=[]
    symlink_list=[]
    file_list=[]
    for item in items:
        item_path = os.path.join(srcPath, item)
        if os.path.isdir(item_path):
            dir_list.append(item)
        elif os.path.islink(item_path):
            symlink_list.append(item)
        elif os.path.isfile(item_path):
            file_list.append(item)
#    print dir_list
#    print file_list

    for directory in dir_list:
        src_dir = os.path.join(srcPath, directory)
        dest_dir = os.path.join(destPath, directory)

        print src_dir
        print u"->"+dest_dir

        # exception?
        os.makedirs(dest_dir)

        listup(srcRoot, destRoot, oldRoot, os.path.join(relativePath, directory))
"""
    for (int i = 0; i < srcDirItems->Length; i++){

        System::String ^ srcItem = srcDirItems[i];

        System::String ^ filename = System::IO::Path::GetFileName(srcItem);

        System::String ^ destItem = System::IO::Path::Combine(destRoot, relativePath, filename);

        System::String ^ oldItem = System::IO::Path::Combine(oldRoot, relativePath, filename);

        System::Console::WriteLine(srcItem);

        // ディレクトリだ。コピーして再帰するぞ。

        try

        {

            System::IO::Directory::CreateDirectory(destItem);

        }

           catch(System::Exception ^ e)

        {

           System::Console::WriteLine(L"An error occurred: '{0}'", e);

        }

            listup(srcRoot, destRoot, oldRoot, System::IO::Path::Combine(relativeP  ath, filename));

        }



        array < System::String ^ > ^ srcFileItems = System::IO::Directory::GetFiles(srcPath);

        for (int i = 0; i < srcFileItems->Length; i + +){

            System::String ^ srcItem = srcFileItems[i];

            System::String ^ filename = System::IO::Path::GetFileName(srcItem);

            System::String ^ destItem = System::IO::Path::Combine(destRoot, relativePath, filename);

            System::String ^ oldItem = System::IO::Path::Combine(oldRoot, relativePath, filename);

            // ファイルだ。ハードリンク必要か調べて、ダメならコピーだ。

            bool hardlinked = false;

            if (System: :IO::File::Exists(oldItem)){

                if (System: : IO::File::Exists(oldItem)){

                    // 古いDestと日付がほぼ一緒で、サイズが同じ

                    System::IO::FileInfo ^ oldfi = gcnew
                    System::IO::FileInfo(oldItem);

                    System::IO::FileInfo ^ srcfi = gcnew
                    System::IO::FileInfo(srcItem);

                    if (oldfi->Length == srcfi->Length){

                        if (oldfi->LastWriteTime.Year == srcfi->LastWriteTime.Year
                            & & oldfi->LastWriteTime.Month == srcfi->LastWriteTime.Month
                            & & oldfi->LastWriteTime.Day == srcfi->LastWriteTime.Day
                             & & oldfi->LastWriteTime.Hour == srcfi->LastWriteTime.Hour
                            & & oldfi->LastWriteTime.Minute == srcfi->LastWriteTime.Minute
                            & & oldfi->LastWriteTime.Second == srcfi->LastWriteTime.Secon)

                        {
                            ATL::CString
                            atlOldItem(oldItem);

                            ATL::CString
                            atlDestItem(destItem);

                            BOOL success =::CreateHardLink(atlDestItem, atlOldItem, NULL);

                            if (success){

                                hardlinked = true;

                                // System::Console::WriteLine(L"HLinked");
                            }

                            else{
                                System::Console::WriteLine(L"Error:HLink");

                                System::Console::WriteLine(destItem);

                            }

                        }

                    }

                }


            }



            if (!hardlinked){

                // System::Console::WriteLine(L"Copy");

                try{

                    System::IO::File::Copy(srcItem, destItem, true);

                }catch(System::Exception ^ e){

                   System::Console::WriteLine(L"An error occurred: '{0}'", e);

                }

            }

        }

    }
"""


if __name__ == "__main__":
    srcRoot = sys.argv[1]  # バックアップ元

    destRoot = sys.argv[2] # バックアップ先

    oldRoot = "" # バックアップ（ふるいの）



    listup(srcRoot, destRoot, oldRoot, u"")

