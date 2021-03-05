/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number}
 */
function toleaf(node, path, sum){
    if(!node){
        return 0
    }
    let ans = 0;
    path.push(0);

    for(let i=0;i<path.length;i++){
        path[i] += node.val;

        if(path[i]==sum){
            ans += 1;
        }
    }
    return ans+toleaf(node.left, Array.from(path), sum)+toleaf(node.right, Array.from(path), sum);
}
var pathSum = function(root, sum) {
    return toleaf(root, [], sum);
};