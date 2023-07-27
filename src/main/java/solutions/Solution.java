package solutions;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution {
    //|0001|Two Sum|
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map=new HashMap<>(nums.length);
        for(int i=0;i<nums.length;i++){
            Integer j=map.get(target-nums[i]);
            if(j!=null){
                return new int[]{i,j};
            }
            map.put(nums[i],i);
        }
        return null;
    }
    //|0002|Add Two Numbers|none|Medium|
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res=new ListNode();
        ListNode p=res;
        ListNode q=null;
        int carry=0;
        while(l1!=null&&l2!=null){
            int val=l1.val+l2.val+carry;
            carry=val/10;
            val%=10;
            p.val=val;
            p.next=new ListNode();
            q=p;
            p=p.next;
            l1=l1.next;
            l2=l2.next;
        }
        while(l1!=null){
            int val=l1.val+carry;
            carry=val/10;
            val%=10;
            p.val=val;
            p.next=new ListNode();
            q=p;
            p=p.next;
            l1=l1.next;
        }
        while(l2!=null){
            int val=l2.val+carry;
            carry=val/10;
            val%=10;
            p.val=val;
            p.next=new ListNode();
            q=p;
            p=p.next;
            l2=l2.next;
        }
        if(carry!=0){
            p.val=carry;
        }
        else{
            q.next=null;
        }
        return res;
    }
    //|0003|Longest Substring Without Repeating Characters|none|Medium|
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set=new HashSet<>(s.length());
        int max=0;
        int left=0,right=0;
        while(left<s.length()){
            if(left>0){
                set.remove(s.charAt(left-1));
            }
            while(right<s.length()&&!set.contains(s.charAt(right))){
                set.add(s.charAt(right++));
            }
            left+=1;
            max=Math.max(max,right-left+1);
        }
        return max;
    }
    //|0004|Median of Two Sorted Arrays|none|Hard|
    private int getKthData(int[] nums1,int[] nums2,int k){
        int i1=0,i2=0;
        while(true){
            if(i1==nums1.length){
                return nums2[i2+k-1];
            }
            if(i2==nums2.length){
                return nums1[i1+k-1];
            }
            if(k<=1){
                return Math.min(nums1[i1],nums2[i2]);
            }
            int halfLength=k/2;
            int temp1=Math.min(i1+halfLength,nums1.length)-1;
            int temp2=Math.min(i2+halfLength,nums2.length)-1;
            if(nums1[temp1]<=nums2[temp2]){
                k-=temp1-i1+1;
                i1=temp1+1;
            }else{
                k-=temp2-i2+1;
                i2=temp2+1;
            }
        }
    }
    //|0004|Median of Two Sorted Arrays|none|Hard|
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int totalLength= nums1.length+nums2.length;
        if((totalLength&1)==0){//偶数
            int mid1=getKthData(nums1,nums2,totalLength>>1);
            int mid2=getKthData(nums1,nums2,(totalLength>>1)+1);
            return (mid1+mid2)/2.0;
        }else{
            return getKthData(nums1,nums2,(totalLength>>1)+1);
        }
    }
}
