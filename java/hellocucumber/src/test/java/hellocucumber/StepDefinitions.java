package hellocucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import static org.junit.Assert.*;

public class StepDefinitions {

    private Double radius;
    private Double area;

    @Given("un radio de valor 5.0")
    public void radius_value_five() {
        this.radius = 5.0;
    }

    @When("al calcular el area")
    public void area_calc() {
        this.area = Math.PI * Math.pow(this.radius, 2);
    }

    @Then("el area es igual a {string}")
    public void area_value_equals_to(String expectedAnswer) {
        assertEquals(expectedAnswer, String.valueOf(this.area));
    }
}
