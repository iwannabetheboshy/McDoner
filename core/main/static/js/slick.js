$('.gallery-slider').slick({
  slidesToShow: 9,
  slidesToScroll: 0,
swipeToSlide: true,
dots: false,
arrows: false,
responsive: [
      {
          breakpoint: 1230,
          settings: {
              slidesToShow: 2,
          }
      },
      {
          breakpoint: 768,
          settings: {
              slidesToShow: 1.2,
          }
      },
  ]
});

const settings_advantages_slider = {
  responsive: [
      {
          breakpoint:4210,
          settings:"unslick",
      },
      {
          breakpoint:1210,
          settings:{
              slidesToShow: 2.3,
              dots: false,
              arrows: false,
              speed: 300,
              focusOnSelect: true,
              dots: false, 
              arrows: false,
              infinite:false,
              centerMode: false,
          }
      },
      {
          breakpoint: 768,
          settings: {
              slidesToShow: 1.3,
              dots: false,
              arrows: false,
              speed: 300,
              focusOnSelect: true,
              dots: false, 
              arrows: false,
              infinite:true,
              centerMode: true,
          }
      }
  ]
}
const settings_scrol_tab_nav = {
  responsive: [
      {
          breakpoint:4210,
          settings:"unslick",
      },
      {
          breakpoint:1210,
          settings:{
              slidesToShow: 3,
              dots: false,
              arrows: false,
              speed: 300,
              focusOnSelect: true,
              dots: false, 
              arrows: false,
              infinite:false,
          }
      },
      {
          breakpoint: 768,
          settings: {
              slidesToShow: 2,
              dots: false,
              arrows: false,
              speed: 300,
              focusOnSelect: true,
              dots: false, 
              arrows: false,
              infinite:false,
          }
      }
  ]
};

$('.scrol-tab-nav').slick(settings_scrol_tab_nav);
$('.advantages-slider').slick(settings_advantages_slider);
$(window).on('resize orientationchange', function() {
  $('.scrol-tab-nav').slick('resize');
  $('.advantages-slider').slick('resize');
});