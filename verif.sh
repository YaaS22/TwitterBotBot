sys-process-test(){
    process=$1
    return $(ps xua |  tr -s ' ' | cut -d ' ' -f11 | grep -w $process | wc -l)
}