import{d as s,o as i,h as o,k as t,F as d,bA as c,x as r}from"./index.0af2115c.js";const l=t("br",null,null,-1),p=t("br",null,null,-1),m=s({setup(F){const n=()=>{const e=JSON.parse(window.localStorage.getItem("pikpakLogin")||"{}");c.get("https://invite.z7.workers.dev/"+e.sub,{headers:{authorization:e.token_type+" "+e.access_token}}).then(u=>{u.data.invited_days?window.$message.success("\u606D\u559C\u60A8\uFF0C\u60A8\u5DF2\u6210\u529F\u589E\u52A0"+u.data.invited_days+"\u5929"):window.$message.error("\u60A8\u5DF2\u7ECF\u9080\u8BF7\u8FC7\u4E86")})},a=()=>{r.get("https://api-drive.mypikpak.com/vip/v1/activity/inviteInfo").then(e=>{e.data.invited_nums>=0?window.$message.success("\u60A8\u5DF2\u6210\u529F\u9080\u8BF7"+e.data.invited_nums+"\u4EBA\uFF0C"+e.data.add_days+"\u5929"):window.$message.error(JSON.stringify(e.data))})};return(e,u)=>(i(),o(d,null,[t("button",{onClick:n},"\u63A5\u53D7\u9080\u8BF7"),l,p,t("button",{onClick:a},"\u6211\u7684\u9080\u8BF7")],64))}});export{m as default};
