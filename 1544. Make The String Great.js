/**
 * @param {string} s
 * @return {string}
 */
 var makeGood = function(s) {
    let cnt = 0;

    while(cnt<s.length-1){
        if(cnt<0){
            cnt += 1;
            continue;
        }
        
        let [cur, next] = [s.charCodeAt(cnt), s.charCodeAt(cnt+1)];
        
        if (((cur>96 && cur<123 && next>64 && next<91) 
           ||(cur>64 && cur<91 && next>96 && next<123))
           &&(Math.abs(cur-next)==32)){

               s = s.slice(0, cnt)+s.slice(cnt+2);
               cnt-=2
        }
        cnt += 1
    }
    return s;
};