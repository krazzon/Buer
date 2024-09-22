import ctypes,os
from time import sleep
from pathlib import Path
tracklist = []

def clear(): os.system("cls")

def start():
    clear()
    os.system("title Buer cd player")
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    input("> press enter when u want to play the cd")
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
    while True:
        try:
            drive = Path("E:\\")
            if not drive:
                break
            else:
                sleep(1)
                drive = Path("E:\\")
                break
        except PermissionError:
            print(f"p denied {drive_path}")
        except Exception as e:
            print(f"err: {e}")
    for i in drive.iterdir():
        if i.is_dir():
            pass
        else:
            tracklist.append(i)
    while True:
        if  os.system("taskkill /f /im Microsoft.Media.Player.exe & cls") == 0: ## real taskill functiom
            break
    os.system("taskkill /f /im explorer.exe") ## laziest fix for da error 
    os.system("start explorer.exe & color 4") ## systerm weird do not add above line or will loop>????
    clear()

    for i in tracklist:
        os.system("color 4")
        print(i)
    os.system("color f")
    _start=input("\n\n* startin trackk : ")
    os.system(f"start wmplayer.exe {_start}")
    clear()
    os.system("color 4 & mode 138,38")
    print("""


                                                           -+-                                                                          
                                                           @+}                                                                          
                                                          .]^]                                                                          
                                                            ^                                                                           
                                                           -]-                                                                          
                                                           ] +                                                                          
                                                           -<  -                                                                        
                                                              - }-                                                                      
                                                               } }                       --                                             
                                               <@@<@@@+        } }                             -#^          .<+                         
                                             <@@@@]< #<        } #    <@<          -#}   --    ] @         -}+]                         
                                           <@}]] @^#@@+        +}+  ]@< @        <@@ ^         ^@-#     <@^ + #                         
                     ^@@                   @#]@@#@< @@]<#^ .^.     }@#^@<      <@@@@@}         -@.@    +@ ^ -+^                         
                     #<@] - -              @@@ ^@} }^.+@@@#@@@@<   @@@@      ]@# <@@-   .@@]   <-@-   +] @..-^^                         
                     ^@# @@@@<             -#+<} @@ @@@@@@@+ -+@ +}@-@@ @@#@]- -@@@@    @@@@   + +  ^< -#.] <                           
                       +^@}<^]  +<+-         @-@@@@^ }@@@@@#@@}.}^ +^@^@@@@@@+@<       @@]@@   }]}^@@^-+   -                            
                        -@@@].] +   .]+    - ^@ }.@ @@^@@@#^+-   --+ @.@@ @^.@<<@<     @-@@@   @@@@+}^-]}^-                             
                         ^@]< ] +  +  ].^-.]@]@]]+@@} ]@     .^^^.-@@@ @@@@}@@@@ <@<  .@<@+-#@@@-]<@#    ++                             
                            +@]- +@@@^<@@@^@@@#@ }@@ @<^.  ^  .  .@# @@@^ ^@@@@+ .^@@<^^@^@@#^  @@+-  <]]^                              
                               .]<@@.@@@}@@@-@@]#@ @ @-  ^^ ^-   ^@+@#<]-. <+@@^ -^@@@}-. @+- @@<< <                                    
                                  <@@@#@-@<@@+- # +^@@ }}@^ ]@.  .@}<@@@# +-@@@@]@}.-}#]  @@ #@]@ }+                                    
                                  .} + @-@@<@. @}.]^^ -}^#@-@<]-  @@@+<@@-..@ <#@@.  @ ##  @@@@< @                                      
                                  ] }}@-@@<<#-]@ }#+-@^ @ @#@<^..+}^-  @@-@@#    ]<< @@]@@<-@@]@@<                                      
                                <@.< @@^@@@@< +] . +}@ +@<@ ^@}@+ +-+  +@<@@@@}.}@@@@@@]@@@                                             
                              ^#] @.#@].-@@@@@@@ <-  <^]@]@- ^@@< < <   @@#]@@@@    ^@ #@@@                                             
                              @ ^@}+@] @@@    @@ @ <}#  #@@]  <}<<+     @@#@ @@@ -@@@@@@ @@                                             
                              @ @  @# @@@@-   +@@] @ @@^  ]@<. ^<< <   ]@#<@@@@ @@<  # @@@< +@^                                         
                              @-##}@-]+<@@<    @# <}+ ]^  <@^^^@<<}  -<@@}@-]@@@@@@ @@@@@<  # @                                         
                              @+ ]@@@@]--@@@@@@@}  +^ ^ @@@+}@@@^@@-}@@+@@+^  ^^<}<@@ ^.    }@<                                         
                              +]}@@#@@#<^. <@@@.@@@@@<@# @<}}-@@@@@@@@# @+]]@@@@^@@^}@  . .-                                            
                                 <@@@@<  .+@@@@@@@<@#@@.@@<^<<@<@-+}@#@+}#+@##]+@]}#}@@@@@@<.                                           
                                      - }@@@.} @@@@@#@@@@]@@]@@@^+ .@@@<^##@@@ .@<]^@@ @@@@@                                            
                                        .< @@@-  @  @^<@@@+@]@<@ <}^-+^]@#]]^@^< @@+-@@@@@@<      }@^                                   
                                    ]@} . ^   .. }]<@<--+@#} @#@@^ ---+}@@-@@@ .@@ - <@}@@    ]@# # #                                   
                                  <@@@@.<- ^   ^@]}}@@@@+.}]]@@@@@<@}@]-@@-@@ #@@-  -]<@<   ]}< @ }@^                                   
                                  @^. @^ @@@]]@@+..}^^@@@@@@@@<# @@<  @@@@@@@##^^#<-  ] @@@.< ^@#                                       
                                  <@@]}@}@]@^<<<@@^ ]. @. @@@}@@@ .@@@@<<@^ -#@@^ ]+]@+ < }<]#-                                         
                                    +@@@@@]@^]@@^   @@<@ ^+ @ ^@@@@@@@@-@@@<@@#}+-@.]^}-@@@+                                            
                                     ^@@@.}@          <@@@] <@] }@@<<}+<@@@@@<@ @@@@@@^                                                 
                                      }@+@                             -@@#+@]-@ @@@@<                                                  
                                      #@+@@                             ^@@@@@@@@} .+#                                                  
                                      ]@@.@@                              -@@-<@ +  ^+.                                                 
                                      -^+@^@                                   }]@@] <@+  .                                             
                                       <#@@@]                                  ^@#.^   @   .                                            
                                        ]@@<+-                                     ^.]@^-<+]   <<                                       
                                           .^]+                                    .<+.+.#.@] -. ^                                      
                                           -@.@ ^]]                                      <@-+. << .                                     
                                            @]<<< ]                                       .}]    .                                      
                                            -]- .]^                                                                                     
                                              .]<                                                                                       

""")

if __name__ == "__main__":
    start()
