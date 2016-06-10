# -*- coding: utf-8 -*-
import sys
import os
import os.path
import time
import shutil

def listup(srcRoot, destRoot, oldRoot, relativePath):

    srcPath = os.path.join(srcRoot, relativePath)
    destPath = os.path.join(destRoot, relativePath)
    oldPath = os.path.join(oldRoot, relativePath)

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

    for file_item in file_list:

        hardlinked = False


        src_file = os.path.join(srcPath, file_item)
        dest_file = os.path.join(destPath, file_item)
        old_file = os.path.join(oldPath, file_item)

        print src_file
        print u"->" + dest_file

        if os.path.exists(old_file):
            old_file_size = os.path.getsize(old_file)
            src_file_size = os.path.getsize(src_file)

            # 古いDestと日付がほぼ一緒で、サイズが同じ
            if old_file_size == src_file_size:
                old_file_last_write_time = time.gmtime(os.path.getmtime(old_file))
                src_file_last_write_time = time.gmtime(os.path.getmtime(src_file))

                # print old_file_last_write_time
                # print src_file_last_write_time
                if old_file_last_write_time.tm_year == src_file_last_write_time.tm_year \
                        and old_file_last_write_time.tm_mon == src_file_last_write_time.tm_mon \
                        and old_file_last_write_time.tm_mday == src_file_last_write_time.tm_mday \
                        and old_file_last_write_time.tm_hour == src_file_last_write_time.tm_hour \
                        and old_file_last_write_time.tm_min == src_file_last_write_time.tm_min \
                        and old_file_last_write_time.tm_sec == src_file_last_write_time.tm_sec:

                    success = True
                    try:
                        os.link(old_file, dest_file)

                    except IOError:
                        success = False

                    if success:
                        print "HLinked"
                        hardlinked = True

        if not hardlinked:
            shutil.copy2(src_file, dest_file)




"""


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

    oldRoot = sys.argv[2]  # バックアップ（ふるいの）

    destRoot = sys.argv[3] # バックアップ先





    listup(srcRoot, destRoot, oldRoot, u"")

