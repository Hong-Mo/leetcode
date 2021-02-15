/**
 * @param {number[][]} grid
 * @return {number}
 */
var largest1BorderedSquare = function(grid) {
    let [dp, max_side] = [[], 0];

    for(let i=0;i<grid.length;i++){
        dp.push([]);

        for(let j=0;j<grid[i].length;j++){
            let acc = [0, 0]

            if(grid[i][j]==1){
                if(i==0){
                    acc[0] = 1;
                }else{
                    acc[0] = dp[i-1][j][0]+1;
                }
                if(j==0){
                    acc[1] = 1;
                }else{
                    acc[1] = dp[i][j-1][1]+1;
                }
                let side = Math.min(...acc);
                max_side = Math.max(1, max_side);

                for(let k=side;k>max_side;k--){
                    if(dp[i][j-(k-1)][0]>=k && dp[i-(k-1)][j][1]>=k){
                        max_side = k;
                        break;
                    }
                }
            }
            dp[i].push(acc);
        }
    }
    return Math.pow(max_side, 2);
};