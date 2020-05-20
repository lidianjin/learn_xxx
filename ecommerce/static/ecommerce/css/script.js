function getTemplateInfo() {
    // 模板介绍
    document.getElementById("template_data").innerHTML = `
        <div class="jumbotron">
          <p class="lead">此模板用于采集京东主页，进行商品关键词搜索后的列表页信息。</p>
          <h1 class="display-4">使用方法：</h1>
          <hr class="my-4">
          <p>1. 点击<b>立即使用</b>进入参数配置界面。</p>
          <p>2. 输入要检索的<b>关键词</b>，如“<b>华为</b>”。</p>
          <p>3. 设置要<b>翻页的次数</b>，即点击下一页的次数。请输入<b>数字</b>，如“5”，可实现只采集前5页的内容。最大值100页。</p>
          <p>4. 所有参数设置完毕后，进行采集。</p>
        </div> 
    `;
}


function getCommentTemplateInfo() {
    // 京东商品评论采集模板介绍
    document.getElementById("comment_template_data").innerHTML = `
        <div class="jumbotron">
          <p class="lead">此模板用于采集京东商品详情页的商品评价信息。</p>
          <h1 class="display-4">使用方法：</h1>
          <hr class="my-4">
          <p>1. 点击<b>立即使用</b>进入参数配置界面。</p>
          <p>2. 输入要采集的<b>商品网址</b>，例如https://item.jd.com/100008384344.html。</p>
          <p>3. 设置要<b>翻页的次数</b>，即点击下一页的次数。请输入<b>数字</b>，如“5”，可实现只采集前5页的内容。最大值100页。</p>
          <p>4. 所有参数设置完毕后，进行采集。</p>
        </div> 
    `;
}


function getTemplateField() {
    // 采集字段预览
    // todo: 默认值，即默认选择‘搜索关键字’并展示对应的图片
    // todo: 被选择时，背景高亮显示
    document.getElementById("template_data").innerHTML = `
        <div id="field_left">
            <div class="list-group">
              <button type="button" class="list-group-item list-group-item-action active" onclick="getSearchKeyWord()">搜索关键词</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getShopName()">商家店名</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getGoodName()">商品名称</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getCommentNumber()">评价人数</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getPrice()">价格</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getDetailLink()">商品详情页链接</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getPage()">页码</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getShopLink()">店铺链接</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getGoodComment()">商品评论链接</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getCover()">封面图链接</button>
            </div>
        </div>
        <div id="field_right">
            <!-- 示例图片 -->
        </div>
        `;
}


function getCommentTemplateField() {
    // 京东商品评论采集字段预览
    document.getElementById("comment_template_data").innerHTML = `
        <div id="field_left_2">
            <div class="list-group">
              <button type="button" class="list-group-item list-group-item-action active" onclick="getUsername()">用户名</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getCommentStar()">评价星级</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getContent()">评价内容</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getCommentTime()">评价时间</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getThumb()">点赞数</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getReComment()">评论数</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getTitle()">页面标题</button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getSite()">页面网址</button>
            </div>
        </div>
        <div id="field_right_2">
            <!-- 示例图片 -->
        </div>
        `;
}


function getUsername() {
    // 用户名
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/username.jpg" alt="用户名_图片加载失败">
        `;
}


function getCommentStar() {
    // 评价星级
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/commentStar.jpg" alt="评价星级_图片加载失败">
        `;
}


function getContent() {
    // 评价内容
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/content.jpg" alt="评价内容_图片加载失败">
        `;
}


function getCommentTime() {
    // 评价时间
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/commentTime.jpg" alt="评价时间_图片加载失败">
        `;
}


function getThumb() {
    // 点赞数
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/thumb.jpg" alt="点赞数_图片加载失败">
        `;
}


function getReComment() {
    // 评论数
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/reComment.jpg" alt="评论数_图片加载失败">
        `;
}


function getTitle() {
    // 页面标题
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/title.jpg" alt="页面标题_图片加载失败">
        `;
}


function getSite() {
    // 页面网址
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/site.jpg" alt="页面网址_图片加载失败">
        `;
}


function getCommentPage() {
    // 翻页次数
    document.getElementById("field_right_2").innerHTML = `
        <img src="/static/ecommerce/images/commentPage.jpg" alt="翻页次数_图片加载失败">
        `;
}


function getSearchKeyWord() {
    // 搜索关键字
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/searchKeyWord.jpg" alt="搜索关键字_图片加载失败">
        `;
}


function getShopName() {
    // 商家店名
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/shopName.jpg" alt="商家店名_图片加载失败">
        `;
}


function getGoodName() {
    // 商品名称
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/goodName.jpg" alt="商品名称_图片加载失败">
        `;
}


function getCommentNumber() {
    // 评价人数
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/commentNumber.jpg" alt="评价人数_图片加载失败">
        `;
}


function getPrice() {
    // 价格
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/price.jpg" alt="价格_图片加载失败">
        `;
}


function getDetailLink() {
    // 商品详情页链接
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/detailLink.jpg" alt="商品详情页链接_图片加载失败">
        `;
}


function getPage() {
    // 页码
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/page.jpg" alt="页码_图片加载失败">
        `;
}


function getShopLink() {
    // 店铺链接
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/shopLink.jpg" alt="店铺链接_图片加载失败">
        `;
}


function getGoodComment() {
    // 商品评论链接
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/goodComment.jpg" alt="商品评论链接_图片加载失败">
        `;
}


function getCover() {
    // 封面图链接
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/cover.jpg" alt="封面图链接_图片加载失败">
        `;
}


function getParameter() {
    // 采集参数
    document.getElementById("template_data").innerHTML = `
        <div class="list-group">
              <button type="button" class="list-group-item list-group-item-action active" onclick="getSearchKeyWord()">
                搜索关键词
              </button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getPage()">页数</button>
        </div>
        <div id="field_right">
            <!-- 示例图片 -->
        </div>
        `;
}


function getCommentParameter() {
    // 京东商品评论采集参数
    document.getElementById("comment_template_data").innerHTML = `
        <div class="list-group">
              <button type="button" class="list-group-item list-group-item-action active" onclick="getSite()">
                输入网址
              </button>
              <button type="button" class="list-group-item list-group-item-action" onclick="getCommentPage()">翻页次数</button>
        </div>
        <div id="field_right_2">
            <!-- 示例图片 -->
        </div>
        `;
}


function getSampleData() {
    // 示例数据
    document.getElementById("template_data").innerHTML = `
        <table border="1">
            <thead>
                <th>搜索关键词</th>
                <th>商家店名</th>
                <th>商品名称</th>
                <th>评价人数</th>
                <th>价格</th>
                <th>商品详情页链接</th>
                <th>页码</th>
                <th>店铺链接</th>
                <th>商品评论链接</th>
                <th>封面图链接</th>
            </thead>
            <tr>
                <td>耐克</td>
                <td>羽怿运动专营店</td>
                <td>耐克AIR JORDAN 1 MID AJ1乔1黑红脚趾小禁穿小碎扣黑曜石复刻男女情侣篮球鞋</td>
                <td>2500+</td>
                <td>1289.00</td>
                <td>https://item.jd.com/28254838398.html</td>
                <td>1</td>
                <td>https://mall.jd.com/index-55010.html</td>
                <td>https://item.jd.com/28254838398.html</td>
                <td>https://img13.360buyimg.com/n7/jfs/t1/65317/3/15320/68261/5dcd29feE78ec895f/21181df34d0c966a.jpg</td>
            </tr>
        </table>
        `;
}


function getCommentSampleData() {
    // 京东商品评论采集示例数据
    document.getElementById("comment_template_data").innerHTML = `
        <table border="1">
            <thead>
                <th>用户名</th>
                <th>评价星级</th>
                <th>评价内容</th>
                <th>评价时间</th>
                <th>点赞数</th>
                <th>评论数</th>
                <th>页面标题</th>
                <th>页面网址</th>
            </thead>
            <tr>
                <td>jd_518029235</td>
                <td>★★★★★</td>
                <td>送给媳妇的礼物 不知道怎么样 支持国货 她用苹果办公不方便，选择华为相信华为手机，体验了一下操作顺滑，无卡顿，相机功能非常强大，拍照清晰，视频通话也很清楚，曲面刘海屏的设计感观非常好，希望华为越来越好！</td>
                <td>2020-02-17 20:37</td>
                <td>39</td>
                <td>12</td>
                <td>华为 HUAWEI Mate 30 Pro 麒麟990旗舰芯片OLED环幕屏双4000万徕卡电影四摄8GB+256GB亮黑色4G全网通游戏手机</td>
                <td>https://item.jd.com/100008384344.html#comment</td>
            </tr>
        </table>
        `;
}


// function downloadXlsFile() {
//     // 下载xls文件
//     window.open("ecommerce/data/jdsearch_data.xls");
//     window.open("requirements.txt");
//     alert("hello world");
//     // var $eleForm = $("<form method='get'></form>");
//     //
// 	// $eleForm.attr("action","ecommerce/data/jdsearch_data.xls");
//     //
// 	// $(document.body).append($eleForm);
//
// 	//提交表单，实现下载
// 	// $eleForm.submit();
// }