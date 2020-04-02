function getTemplateInfo() {
    // 模板介绍
    document.getElementById("template_data").innerHTML = `
        <p>此模板用于采集京东主页，进行商品关键词搜索后的列表页信息。</p>
        <h2>使用方法：</h2>
        <p>1. 点击<b>立即使用</b>进入参数配置界面。</p>
        <p>2. 输入要检索的<b>关键词</b>，如“<b>华为</b>”。</p>
        <p>3. 设置要<b>翻页的次数</b>，即点击下一页的次数。请输入<b>数字</b>，如“5”，可实现只采集前5页的内容。</p>
        <p>4. 所有参数设置完毕后，进行采集。</p> 
        `;
}


function getTemplateField() {
    // 采集字段预览
    document.getElementById("template_data").innerHTML = `
        <div id="field_left">
            <ul>
                <li onclick="getSearchKeyWord()">搜索关键词</li>
                <li>商家店名</li>
                <li>商品名称</li>
                <li>评价人数</li>
                <li>价格</li>
                <li>商品详情页链接</li>
                <li>页码</li>
                <li>店铺链接</li>
                <li>商品评论链接</li>
                <li>封面图链接</li>
            </ul>
        </div>
        <div id="field_right">
            <!-- 示例图片 -->
        </div>
        `;
}


function getSearchKeyWord() {
    // 搜索关键字
    document.getElementById("field_right").innerHTML = `
        <img src="/static/ecommerce/images/searchKeyWord.jpg" alt="搜索关键字_图片加载失败">
        `;
}


function getParameter() {
    // 采集参数
    document.getElementById("template_data").innerHTML = `
        <div>
            <ul>
                <li onclick="getSearchKeyWord()">搜索关键词</li>
                <li>页数</li>
            </ul>
        </div>
        <div id="field_right">
            <!-- 示例图片 -->
        </div>
        `;
}


function getSampleData() {
    // 示例数据
    document.getElementById("template_data").innerHTML = `
        <table border="1">
            <thead>
                <td>搜索关键词</td>
                <td>商家店名</td>
                <td>商品名称</td>
                <td>评价人数</td>
                <td>价格</td>
                <td>商品详情页链接</td>
                <td>页码</td>
                <td>店铺链接</td>
                <td>商品评论链接</td>
                <td>封面图链接</td>
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