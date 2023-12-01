# simpleGUI for whisper-standalone-win


An easy-to-use GUI addon for [whisper-standalone-win](https://github.com/Purfview/whisper-standalone-win) that includes a built-in YouTube video downloader. The downloader also recognizes downloaded videos to be processed with `whisper-standalone-win`.

  ![Whisper-Faster-simpleGUI](https://github.com/Adamsw72/whisper-standalone-win-simpleGUI/assets/37792924/3063501a-3be7-487d-8ea1-ff814073ec4b)

This is my first script written in Python. Any feedback or suggestions are greatly appreciated!

# Features

- **GUI Addon for Whisper-Standalone-Win**: Provides a user-friendly graphical interface for `whisper-standalone-win`, making it easier and faster to use.
- **Drag-and-Drop**: Includes a drag-and-drop feature for file handling. This allows you to simply drag a file from your file explorer and drop it into the program window to load it.
- **YouTube Video Downloader**: Allows you to download videos directly from YouTube within the application, and prepares them for processing with `whisper-standalone-win`.

# Requirements

- Windows operating system x64 (tested at W11 Pro)
- [`faster-whisper`](https://github.com/SYSTRAN/faster-whisper) installed
- [`whisper-standalone-win`](https://github.com/Purfview/whisper-standalone-win) installed

# Installation

To install it correctly just put the Simple GUI to the directory of `faster-whisper` and `whisper-standalone-win`

# Usage

Once you have correctly installed Simple GUI,`faster-whisper` and `whisper-standalone-win` you can start the application by launching Simple-GUI.exe. To process a file, simply drag and drop it into the application window. The file will be processed by `whisper-standalone-win` and `faster-whisper`.

Similarly, if you download a video from YouTube using the application, it will automatically be processed. The downloaded YouTube video will be saved in the default Windows Downloads folder. The processed transcription or translation will be saved in the same directory as Simple GUI, `faster-whisper`, and `whisper-standalone-win`

# Menu options

**Task :**

  Qouting from `whisper-standalone-win`
  >Transribe : Whether to perform X->X speech recognition

  >Translate : X->English translation 

**Ai Model :**

large-v3 : More accurate and sensitive to sounds, and it can sometimes recognize abbreviations of words. For example, in Indonesian, “Pilpres” is an abbreviation for “Pemilihan Presiden”, which translates to “Presidential Election” in English. However, the script operates at a slower pace. best for perfect transcribe or translations.

medium : Much faster and good enough for transribe or translations.

**Language :**

The output of the transcription or translation process is determined by the language selection from the dropdown menu. If the desired language is not available in the dropdown menu, it can be manually typed in.

The available languages are as per the specifications of `whisper-standalone-win`:

<details>
  <summary>Language</summary>

>{af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,yue,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Cantonese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Mandarin,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}, -l {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,yue,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Cantonese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Mandarin,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}

</details>
                       
