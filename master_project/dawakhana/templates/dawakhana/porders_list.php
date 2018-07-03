<?php
error_reporting(0);
require('../class/call.php');
?>
<!doctype html>
<html lang="en">
<head>
		<!-- Basic page needs
		============================================ -->
		<title>Pharacist Account</title>
		<meta charset="utf-8">
		<meta name="author" content="">
		<meta name="description" content="">
		<meta name="keywords" content="">

		<!-- Mobile specific metas
		============================================ -->
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
		{% include 'dawakhana/inc/base_link.php' %}
		<script>

			$(document).ready(function(){

				$("body").queryLoader2({
	    			barHeight : 4,
	    			backgroundColor : '#fff',
	    			barColor : '#018bc8',
	    			minimumTime : 2000,
	    			onComplete : function(){

						// show promo popup
	    				if($.arcticmodal && $('body').hasClass('promo_popup')){
							$.arcticmodal({
								url : "modals/promo.html"
							});
						}

	    			}
	    		});

			});

		</script>

		<!-- Old IE stylesheet
		============================================ -->
		<!--[if lte IE 9]>
			<link rel="stylesheet" type="text/css" href="../css/oldie.css">
		<![endif]-->
	</head>


	<body>

		<!-- - - - - - - - - - - - - - Styleswitcher - - - - - - - - - - - - - - - - -->



		<!-- - - - - - - - - - - - - - end Styleswitcher - - - - - - - - - - - - - - - - -->

		<!-- - - - - - - - - - - - - - Main Wrapper - - - - - - - - - - - - - - - - -->

		<div class="wide_layout">

			<!-- - - - - - - - - - - - - - Header - - - - - - - - - - - - - - - - -->

			{% include 'dawakhana/inc/header.php' %}

			<!-- - - - - - - - - - - - - - End Header - - - - - - - - - - - - - - - - -->

			<!-- - - - - - - - - - - - - - Page Wrapper - - - - - - - - - - - - - - - - -->

			<div class="secondary_page_wrapper">

				<div class="container">

					<!-- - - - - - - - - - - - - - Breadcrumbs - - - - - - - - - - - - - - - - -->

					<ul class="breadcrumbs">

						<li><a href="index.html">Home</a></li>
						<li>My Orders</li>

					</ul>

					<!-- - - - - - - - - - - - - - End of breadcrumbs - - - - - - - - - - - - - - - - -->

					<div class="row">

						<aside class="col-md-3 col-sm-4">

							<!-- - - - - - - - - - - - - - Information - - - - - - - - - - - - - - - - -->

							{% include 'dawakhana/inc/pharmacist_left.php' %}<!--/ .section_offset -->

							<!-- - - - - - - - - - - - - - End of information - - - - - - - - - - - - - - - - -->

							<!-- - - - - - - - - - - - - - Banner - - - - - - - - - - - - - - - - -->



							<!-- - - - - - - - - - - - - - End of banner - - - - - - - - - - - - - - - - -->

						</aside><!--/ [col]-->

						<main class="col-md-9 col-sm-8">

							<h1>My Orders</h1>

							<header class="top_box on_the_sides">

								<div class="left_side v_centered">

									<p class="visible_pages">Showing 1 to 10 of 30 (3 pages)</p>

									<span>Show:</span>

									<div class="custom_select">

										<select name="">

											<option value="10">10</option>
											<option value="9">9</option>
											<option value="8">8</option>
											<option value="7">7</option>
											<option value="6">6</option>
											<option value="5">5</option>
											<option value="4">4</option>
											<option value="3">3</option>
											<option value="2">2</option>
											<option value="1">1</option>

										</select>

									</div>

								</div>

								<div class="right_side">

									<ul class="pags">

										<li><a href="#"></a></li>
										<li class="active"><a href="#">1</a></li>
										<li><a href="#">2</a></li>
										<li><a href="#">3</a></li>
										<li><a href="#"></a></li>

									</ul>

								</div>

							</header><!--/ .top_box -->

							<div class="table_wrap">

								<table class="table_type_1 orders_table">

									<thead>

										<tr>

											<th class="order_number_col">Order Number</th>
											<th>Order Date</th>
											<th class="ship_col">Ship To</th>
											<th>Order Status</th>
											<th class="order_total_col">Total</th>
											<th></th>

										</tr>

									</thead>

									<tbody>

										<tr>

											<td data-title="Order Number"><a href="#">145000007</a></td>

											<td data-title="Order Date">9/5/2018</td>

											<td data-title="Ship To">John Doe</td>

											<td data-title="Order Status">Pending</td>

											<td data-title="Total" class="total"><i class="icon-rupee"></i>5.99</td>

											<td data-title="Action">

												<ul class="buttons_col">

													<li>

														<a href="order_details.php" class="button_grey" style="font-size: 13px;padding: 3px 10px;">View</a>

													</li>

												</ul>

											</td>

										</tr>

										<tr>

											<td data-title="Order Number"><a href="#">145000007</a></td>

											<td data-title="Order Date">9/5/2018</td>

											<td data-title="Ship To">John Doe</td>

											<td data-title="Order Status">Pending</td>

											<td data-title="Total" class="total"><i class="icon-rupee"></i>5.99</td>

											<td data-title="Action">

												<ul class="buttons_col">

													<li>

														<a href="order_details.php" class="button_grey" style="font-size: 13px;padding: 3px 10px;">View</a>

													</li>

												</ul>

											</td>

										</tr>

										<tr>

											<td data-title="Order Number"><a href="#">145000007</a></td>

											<td data-title="Order Date">9/5/2018</td>

											<td data-title="Ship To">John Doe</td>

											<td data-title="Order Status">Pending</td>

											<td data-title="Total" class="total"><i class="icon-rupee"></i>5.99</td>

											<td data-title="Action">

												<ul class="buttons_col">

													<li>

														<a href="order_details.php" class="button_grey" style="font-size: 13px;padding: 3px 10px;">View</a>

													</li>

												</ul>

											</td>

										</tr>

										<tr>

											<td data-title="Order Number"><a href="#">145000007</a></td>

											<td data-title="Order Date">9/5/2018</td>

											<td data-title="Ship To">John Doe</td>

											<td data-title="Order Status">Pending</td>

											<td data-title="Total" class="total"><i class="icon-rupee"></i>5.99</td>

											<td data-title="Action">

												<ul class="buttons_col">

													<li>

														<a href="order_details.php" class="button_grey" style="font-size: 13px;padding: 3px 10px;">View</a>

													</li>

												</ul>

											</td>

										</tr>

										<tr>

											<td data-title="Order Number"><a href="#">145000007</a></td>

											<td data-title="Order Date">9/5/2018</td>

											<td data-title="Ship To">John Doe</td>

											<td data-title="Order Status">Pending</td>

											<td data-title="Total" class="total"><i class="icon-rupee"></i>5.99</td>

											<td data-title="Action">

												<ul class="buttons_col">

													<li>

														<a href="order_details.php" class="button_grey" style="font-size: 13px;padding: 3px 10px;">View</a>

													</li>



												</ul>

											</td>

										</tr>

									</tbody>

								</table>

							</div>



						</main><!--/ [col]-->

					</div><!--/ .row-->

				</div><!--/ .container-->

			</div><!--/ .page_wrapper-->

			<!-- - - - - - - - - - - - - - End Page Wrapper - - - - - - - - - - - - - - - - -->

			<!-- - - - - - - - - - - - - - Footer - - - - - - - - - - - - - - - - -->

			{% include 'dawakhana/inc/footer.php' %}

			<!-- - - - - - - - - - - - - - End Footer - - - - - - - - - - - - - - - - -->

		</div><!--/ [layout]-->

		<!-- - - - - - - - - - - - - - End Main Wrapper - - - - - - - - - - - - - - - - -->

		<!-- Include Libs & Plugins
		============================================ -->

	</body>

</html>
